import tiktoken
from openai import OpenAI


client = OpenAI(api_key="KEY_API")
 
token_cost_per_million = 0.150  
output_token_cost_per_million = 0.600

def chatbot():
    messages = [
        {"role": "system",
         "content": "You are a helpful assistant who provides concise and to-the-point answers."}
    ]
    all_tokens = 0
    total_input_tokens = 0
    total_output_tokens = 0
    total_context_tokens = 0

    for i in range(3):
        user_input = input(f"Input {i + 1}: ")
        encoding = tiktoken.encoding_for_model("gpt-4o-mini")

        context_tokens = len(encoding.encode(' '.join([msg['content'] for msg in messages])))
        total_context_tokens += context_tokens

        messages.append({"role": "user",
                         "content": user_input})

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=100
        )

        assistant_response = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_response})

        print(f"Assistant: {assistant_response}")


        total_completion_tokens = completion.usage.total_tokens
        all_tokens += total_completion_tokens
        input_tokens = len(encoding.encode(user_input))
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


chatbot()
