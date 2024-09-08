import openai

openai.api_key = 'API_KEY'

def get_bus_info(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant knowledgeable about bus information."},
            {"role": "user", "content": question}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()

def chat():
    print("Welcome to the Bus Information Chatbot!")
    print("Ask me anything about buses, or type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        print(f"Bot: {get_bus_info(user_input)}")

if __name__ == "__main__":
    chat()
