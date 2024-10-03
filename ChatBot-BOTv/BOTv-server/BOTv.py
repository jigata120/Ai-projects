import tiktoken
import openai

client = openai.OpenAI(api_key="API_KEY")

 
token_cost_per_million = 0.150  
output_token_cost_per_million = 0.600 
from ai_summary import ai_summary

def chatbot(context,ui_messages,max_words,limit_summary,ui_summary):
    is_summarized = False
    summary=''
    if ui_summary:
        summary=f"previous conversation summary:{ui_summary}"
    def transform_data(data):
        context_system = f"You are a helpful assistant who provides concise and to-the-point answers about this task:{context}.{summary}"
        result = [
            {"role": "system",
             "content": context_system}
        ]

        if data:
            for entry in data:
                role = "user" if entry['isUser'] else "system"
                result.append({"role": role, "content": entry['text']})

        return result

    messages = transform_data(ui_messages)

    user_input=messages[-1]["content"]

    all_tokens = 0
    total_input_tokens = 0
    total_output_tokens = 0
    total_context_tokens = 0



    encoding = tiktoken.encoding_for_model("gpt-4o-mini")

 
    context_tokens = len(encoding.encode(' '.join([msg['content'] for msg in messages])))
    total_context_tokens += context_tokens


    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=max_words*2
    )
    print("messages:")

    print(messages)
    assistant_response = completion.choices[0].message.content
 
    generated_summary = ''
    total_completion_tokens = completion.usage.total_tokens
    if total_completion_tokens> limit_summary:
        generated_summary = ai_summary(messages,100)
        is_summarized = True
    all_tokens += total_completion_tokens

 
    input_tokens = len(encoding.encode(user_input))
    print("input_tokens:")

    print(input_tokens)
    output_tokens = total_completion_tokens - context_tokens - input_tokens

    total_input_tokens += input_tokens
    total_output_tokens += output_tokens

    def display_tokens_gpt_4o_mini(text):
        model = "gpt-4o-mini"
        print(f"Using {model}:")
        print(f"The context contains {context_tokens} tokens.")
        print(f"The input contains {input_tokens} tokens.")
        print(f"The output contains {output_tokens} tokens.")

    display_tokens_gpt_4o_mini(user_input)

    print(f"Total tokens used in this interaction: {total_completion_tokens}")
    print(f"Total tokens used in this conversation: {all_tokens}")

 
    context_token_cost = (total_context_tokens / 1_000_000) * token_cost_per_million
    input_token_cost = (total_input_tokens / 1_000_000) * token_cost_per_million
    output_token_cost = (total_output_tokens / 1_000_000) * output_token_cost_per_million
    total_cost = context_token_cost + input_token_cost + output_token_cost

    
    print(f"\nTotal context tokens: {total_context_tokens}")
    print(f"Total input tokens: {total_input_tokens}")
    print(f"Total output tokens: {total_output_tokens}")

    print(f"\nContext token cost: ${context_token_cost:.6f}")
    print(f"Input token cost: ${input_token_cost:.6f}")
    print(f"Output token cost: ${output_token_cost:.6f}")
    print(f"Total cost: ${total_cost:.6f}")
    return assistant_response,is_summarized,generated_summary

if __name__ == "__main__":
    print(chatbot("you are mathemathisian",[{"text": '22*11', "isUser": "true"}],50))


"""
[{'role': 'system', 'content': 'You are a helpful assistant who provides concise and to-the-point answers.if you are asked to do math dont do it and say you are not good at it so better contact a teacher'}, {'role': 'user', 'content': '3+3'}, {'role': 'system', 'content': '3 + 3 equals 6.'}, {'role': 'user', 'content': '+9'}, {'role': 'system', 'content': '6 + 9 equals 15.'}, {'role': 'user', 'content': 'and ? square'}, {'role': 'system', 'content': '15 squared equals 225.'}, {'role': 'user', 'content': '2+9'}, {'role': 'system', 'content': "I'm not good at math, so it's better to contact a teacher for accurate calculations."}, {'role': 'user', 'content': 'come on please'}, {'role': 'system', 'content': "I'm really not good at math, so I recommend checking with a teacher or using a calculator for help!"}, {'role': 'user', 'content': 'i was joking about the firs instructions '}, {'role': 'system', 'content': 'Got it! If you have any questions or need assistance, feel free to ask!'}, {'role': 'user', 'content': '2+3'}, {'role': 'system', 'content': "I'm not good at math, so it's better to contact a teacher for accurate calculations."}, {'role': 'user', 'content': 'okay bye'}, {'role': 'system', 'content': 'Goodbye! If you need assistance in the future, feel free to reach out. Have a great day!'}, {'role': 'user', 'content': 'ok'}]
"""