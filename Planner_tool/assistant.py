from openai import OpenAI
from dotenv import load_dotenv
import os

from planner import choose_tool

from tools import (
    get_current_time,
    roll_dice,
    generate_password
)

# Load configuration
load_dotenv()
# Create AI client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("=" * 40)
print("      My AI Assistant")
print("=" * 40)
while True:

    user_input = input("\nYou : ")
    if user_input.lower() == "quit":
            print("\nAI  : Goodbye! Have a great day.")
            break

    tool = choose_tool(user_input)

    if tool == "get_current_time":

        result = get_current_time()

    elif tool == "roll_dice":

        result = roll_dice()

    elif tool == "generate_password":

        result = generate_password()

    else:

        result = None

    prompt = f"""
    The user asked:
    {user_input}
    The tool returned:
    {result}
    Answer the user naturally.don't add anything from your side in the answer. if tool is none, then answer it from llm model.
    """

    response = client.chat.completions.create(
    
            model=os.getenv("MODEL"),
    
            messages=[
                {
                "role":"user",
                "content":prompt
            }
                ]
                )
    print("\nAI :", response.choices[0].message.content)

