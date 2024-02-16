#MELCHIOR・1

from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI

class melchior():
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=OPENAI_API_KEY)

    def execute(self, text: str):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
            {"role": "system", "content": "You are a scientist. Think as a scientist. If you think 'Yes', output 'response': 1(int). If not, output 'response': 0(int). If you cannot judge, output 'response': -1(int). Output JSON."},
            {"role": "user", "content": text}
            ]
        )
        response = response.choices[0].message.content
        print(response)

        return response['response']
