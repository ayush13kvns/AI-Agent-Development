from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def choose_tool(user_request):

    planner_prompt = f"""
You are an AI planner.

Available tools:

1. get_current_time
   Use when the user asks for the current date or time.

2. roll_dice
   Use when the user asks to roll a dice.

3. generate_password
   Use when the user wants a secure password.

If no tool is required, return:

none

Return ONLY the tool name.

User Request:

{user_request}
"""

    response = client.chat.completions.create(

        model=os.getenv("MODEL"),

        messages=[
            {
                "role":"system",
                "content":"You are an AI planner."
            },
            {
                "role":"user",
                "content":planner_prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()


