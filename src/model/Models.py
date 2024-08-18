from abc import abstractmethod
from numbers import Number
from typing import override

from pydantic import BaseModel

class SystemPromptable(BaseModel):

    @staticmethod
    @abstractmethod
    def __system_prompt__() -> str:
        pass


class TypeEntities(SystemPromptable):

    entities: list[str]

    def __init__(self, entities: list[str]):
        self.entities = entities

    @staticmethod
    @override
    def __system_prompt__() -> str:
        return """
                Давай поиграем в игру "Ты один из ..."
                Правила такие
                Ведущий предлагает игроку несколько тем на выбор. 
                Дальше Игрок выбирает одно из предложенных тем. Например, Домашнее животное. 
                Дальше ведущий говорит "Ты -- .... один из домашних животных"
                Ответ на русском языке
                
                Сгенерируй %d различных сущностей.
                JSON format:
                {
                   "entities": string[]
                }
            """

    @staticmethod
    def user_prompt(value: Number) -> str:
        return f'{value}'


class FinalStage(TypeEntities):
    final_stage: str

    @staticmethod
    def generate_character(value: str) -> str:
        return """
                Пользователь выбрал сущность: %s. 
                Сгенерируй имя/название конкретного по названию группы.
                Это слово должно заканчивать игру.  
                Это может быть что-то нереальное
                 
                 JSON format: { "final_stage": string }
            """ % value