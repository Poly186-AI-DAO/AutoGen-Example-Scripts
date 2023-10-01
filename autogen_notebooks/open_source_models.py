import json
from flaml import autogen

def text_completion(prompt):
    response = autogen.oai.Completion.create(
        config_list=[
            {
                "model": "chatglm",
                "api_base": "http://localhost:8080/v1",
                "api_type": "open_ai",
                "api_key": "NULL",  # just a placeholder
            }
        ],
        prompt=prompt,
    )
    return response

def chat_completion(message):
    response = autogen.oai.ChatCompletion.create(
        config_list=[
            {
                "model": "chatglm",
                "api_base": "http://localhost:8080/v1",
                "api_type": "open_ai",
                "api_key": "NULL",
            }
        ],
        messages=[{"role": "user", "content": message}]
    )
    return response

if __name__ == "__main__":
    print("Choose a function to run:")
    print("1. Text Completion")
    print("2. Chat Completion")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        prompt = input("Enter your text for completion: ")
        response = text_completion(prompt)
        print(response)
    elif choice == "2":
        message = input("Enter your chat message: ")
        response = chat_completion(message)
        print(response)
    else:
        print("Invalid choice!")
