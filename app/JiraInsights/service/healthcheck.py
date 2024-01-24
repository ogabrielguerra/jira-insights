from app.JiraInsights.model.core_model import CoreModel


class Healthcheck:

    def __init__(self) -> None:
        self.__CORE_MODEL = CoreModel()
        self.__COLLECTION_HEALTHCHECK = 'healthcheck'

    def insert(self) -> object:
        data = {"sample": "data"}
        return self.__CORE_MODEL.insert_one(data, self.__COLLECTION_HEALTHCHECK)
