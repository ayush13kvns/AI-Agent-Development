from openai import OpenAI
from dotenv import load_dotenv
import os

from tools import (
    get_current_time,
    roll_dice,
    generate_password,read_text_file)

from tool_manager import execute_tool


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

roles = {
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",

    "2": "You are a senior Python developer. Explain programming concepts clearly and always include Python examples.",

    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",

    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",

    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}


print("\nChoose Your Assistant\n")

print("1. Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")

choice = input("\nEnter your choice : ")

messages = [
    {
        "role": "system",
        "content": roles.get(
            choice,
            "You are a helpful AI assistant."
        )
    }
]


while True:

    user_input = input("\nYou : ")
    # Save the user's message

    text = user_input.lower()

    if text.startswith("summarize "):
        filename = user_input[10:].strip()
        file_content = read_text_file(
    	"data/" + filename
	    )

        prompt = f"""
        Summarize the following document.

        Document:

        {file_content}
        """

        response = client.chat.completions.create(

        model=os.getenv("MODEL"),

        messages=[

        {
            "role":"system",
            "content":"You are a helpful assistant."
        },

        {
            "role":"user",
            "content":prompt
        }

        ]

        )

        print(response.choices[0].message.content)
        continue

    if text.startswith("explain"):
        filename = user_input[8:].strip()
        file_content = read_text_file(
        "data/" + filename
        )

        prompt = f"""
        Explain the following document.

        Document:

        {file_content}
        """

        response = client.chat.completions.create(

        model=os.getenv("MODEL"),

        messages=[

        {
            "role":"system",
            "content":"You are a helpful assistant."
        },

        {
            "role":"user",
            "content":prompt
        }

        ]

        )

        print(response.choices[0].message.content)
        continue


    
    if text.startswith("ask"):
        parts = user_input.split(maxsplit=2)
        #print(parts)
        filename = parts[1]
        question = parts[2]

        file_content = read_text_file(
        "data/" + filename
        )

        prompt = f"""
You are given a document.

Answer the user's question using
only the information present
in the document.

If the answer is not available,
say:
'I couldn't find that information
in the document.'

Document:

{file_content}

Question:

{question}
"""



        response = client.chat.completions.create(

        model=os.getenv("MODEL"),

        messages=[

        {
            "role":"system",
            "content":"You are a helpful assistant."
        },

        {
            "role":"user",
            "content":prompt
        }

        ]

        )

        print(response.choices[0].message.content)
        continue


    

    tool_result = execute_tool(user_input)

    if tool_result:

        print("\nAI :", tool_result)

        continue

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )

    ai_reply = response.choices[0].message.content

    print("\nAI :", ai_reply)

    # Save the AI's reply
    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    