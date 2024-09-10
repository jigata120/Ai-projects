import tiktoken
from openai import OpenAI


client = OpenAI(api_key="KEY_API")
 
def chatbot():
    
    messages = [
        {"role": "system",
         "content": "You are a helpful assistant who provides concise and to-the-point answers."}
    ]
    all_tokens = 0


    for i in range(3):
        user_input = input(f"Input {i+1}: ")
        encoding = tiktoken.encoding_for_model("gpt-4o-mini")
        context_tokens = len(encoding.encode(' '.join([msg['content'] for msg in messages])))

        messages.append({"role": "user",
                         "content": user_input})

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens = 100#example restriction
        )

        assistant_response = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_response})

        print(f"Assistant: {assistant_response}")


        # Display the total token usage
        total_completion_tokens = completion.usage.total_tokens
        all_tokens+=total_completion_tokens
        def display_tokens_gpt_4o_mini(text):
            model = "gpt-4o-mini"
            encoding = tiktoken.encoding_for_model(model)
            tokens = encoding.encode(text)

            input_tokens = len(tokens)
            output_tokens=total_completion_tokens-context_tokens-input_tokens

            print(f"Using {model}:")
            print(f"The context contains {context_tokens} tokens.")
            print(f"The input contains {input_tokens} tokens.")
            print(f"The output contains {output_tokens} tokens.")

        display_tokens_gpt_4o_mini(user_input)

        print(f"Total tokens used in this interaction: {total_completion_tokens}")
        print(f"Total tokens used in this conversation: {all_tokens}")


 
chatbot()
