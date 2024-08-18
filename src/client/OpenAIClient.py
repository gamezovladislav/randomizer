import os
from numbers import Number
import json
from tokenize import String

from dotenv import load_dotenv
from openai import OpenAI

from src.model.Models import TypeEntities, SystemPromptable, FinalStage

load_dotenv()

class OpenAIClient:

    def __init__(self):
        self.client = OpenAI()
        self.client.api_key = os.getenv('OPENAI_API_KEY')

    def generateEntities(self, size: Number) -> list[str]:
        result = self.send_request(
            prompt=TypeEntities.user_prompt(size),
            type=TypeEntities
        )
        print(result)
        return result['entities']

    def generate_character(self, value):
        result = self.send_request(
            prompt=FinalStage.generate_character(value),
            type=FinalStage
        )
        print('result!!!!', result)
        return result['final_stage']

    def send_request(self, prompt: str, type: SystemPromptable) -> SystemPromptable:
        message = self.client.beta.chat.completions.parse(
            model='gpt-4o-mini',
            temperature=1,
            messages=[
                { 'role': 'system', 'content': type.__system_prompt__() },
                { 'role': 'user', 'content': prompt },
            ],
            response_format={ 'type': 'json_object' }
        )
        print(message)
        return json.loads(message.choices[0].message.content)

