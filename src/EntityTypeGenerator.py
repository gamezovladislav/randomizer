from numbers import Number

from src.client.OpenAIClient import OpenAIClient


class EntityTypeGenerator:
    def __init__(self):
        self.openAiClient = OpenAIClient()

    def generateArray(self, size: Number = 20):
        entities = self.openAiClient.generateEntities(size)
        print(len(entities))
        return entities

    def sayYouAre(self, value):
        return self.openAiClient.generate_character(value)