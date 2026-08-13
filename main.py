import os
import argparse
import sys
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("env variable not found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1", 
    api_key=api_key
    )


def main():
    print("\nHello from project-zbot!\n")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    
    messages = [
    {"role": "user", "content": args.user_prompt},
    ]
    def generate_content(client, messages):
        # "openrouter/free" is the model used in the assignment
        # if random models are terrible use "openai/gpt-oss-20b:free"
        response = client.chat.completions.create(
            model = "openai/gpt-oss-20b:free",
            messages = messages
        )
        if response.usage is None:
            raise RuntimeError("API request failed")
        return response
    
    response = generate_content(client, messages)
    
    prompt_tokens = response.usage.prompt_tokens
    response_tokens = response.usage.completion_tokens

    if args.verbose == True:
        print(f"User prompt: \n{args.user_prompt}\n")
        print(f"\nPrompt tokens: {prompt_tokens}\n"
              f"Response tokens: {response_tokens}\n")
        print("Response:")
        print(response.choices[0].message.content)
    else:
        print(response.choices[0].message.content)
        



   


if __name__ == "__main__":
    main()
