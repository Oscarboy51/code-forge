import litellm
import os
from dotenv import load_dotenv
load_dotenv()

#  configuring litellm with key

litellm.api_key = os.getenv("sk-uOUPzge98Gq7A2U5FcB6sQ")

def generate_case_summary(notes:str) -> str:
    response = litellm.completion(
        model = "gpt-4",
        messages = [
            {"role": "system", "content": "You are surgical assistant.Summarize the surgical case."},
            {"role": "user", "content":notes}
        ],
        max_tokens = 300

    )

    return response.choices[0].message.content