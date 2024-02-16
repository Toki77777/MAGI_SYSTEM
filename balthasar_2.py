#BALTHASAR・2

from dotenv import load_dotenv
load_dotenv()

import os, json, asyncio
from openai import OpenAI

class balthasar:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=OPENAI_API_KEY)

    async def execute(self, text: str):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
            messages=[
            {"role": "system", "content": "You are a mother. Think as a mother. If you think 'Yes', output 'response': 1(int). If not, output 'response': 0(int). If you cannot judge, output 'response': -1(int). Output JSON."},
            {"role": "user", "content": text}
            ]
        )

        print(response)
        try:
            response = json.loads(response.choices[0].message.content)
            result = int(response['response'])
        except:
            result = 500
        print(response)

        print('BALTHASAR・2 task completed.')
        return result
