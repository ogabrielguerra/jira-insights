from app.JiraInsights.model.core_model import CoreModel


class DataService:

    def __init__(self) -> None:
        self.__CORE_MODEL = CoreModel()
        self.__ISSUE = 'issue'
        self.__PROJECT = 'project'

    def get_sprint_issues(self, sprint_reference: str) -> dict:
        query = {"fields.customfield_10005": {"$regex": sprint_reference}}
        return self.__CORE_MODEL.get_data_by_query('issue', query)

    def get_project_metadata(self) -> dict:
        query = {}
        return self.__CORE_MODEL.get_data_by_query('project', query)

    def insert_issues(self, issue_documents: dict) -> object:
        return self.__CORE_MODEL.insert_many(issue_documents, self.__ISSUE)

    def upsert_issues(self, issue_collections: dict) -> list:
        return self.__CORE_MODEL.upsert_many(issue_collections, self.__ISSUE)

    def insert_project(self, project: dict) -> object:
        return self.__CORE_MODEL.insert_one(project, self.__PROJECT)

    def upsert_project(self, project: dict) -> object:
        return self.__CORE_MODEL.upsert_many(project, self.__PROJECT)

    def drop_collection(self, collection_reference: str) -> bool:
        return self.__CORE_MODEL.drop_collection(collection_reference)

    def get_data_by_query(self, collection_reference: str, query: dict) -> dict:
        return self.__CORE_MODEL.get_data_by_query(collection_reference, query)
