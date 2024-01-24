from os import environ
import requests

from requests import Response
from requests.auth import HTTPBasicAuth
from app.JiraInsights.model.query_handler import QueryHandler
from app.JiraInsights.utils import DotSyntax


class CoreService:

    def __init__(self) -> None:
        self.__JIRA_SERVER_TYPE = DotSyntax({
            'on_premise': 'on_premise',
            'cloud': 'cloud'
        })
        self.__JIRA_DEFAULT_SERVER_TYPE = self.__JIRA_SERVER_TYPE.on_premise

        self.__JIRA_API_BASE_URL = environ['JIRA_API_URL']
        self.__DEFAULT_PROJECT_ID = 'VOLTRON'
        self.__APP_TOKEN = environ['APP_TOKEN']
        self.__AUTH = HTTPBasicAuth(environ['APP_USER'], environ['APP_TOKEN'])

    def get_base_url(self) -> str:
        return self.__JIRA_API_BASE_URL

    def set_base_url(self, url: str):
        self.__JIRA_API_BASE_URL = url

    def get_auth(self) -> str:
        return str(self.__AUTH)

    def get_default_project_id(self) -> str:
        return self.__DEFAULT_PROJECT_ID

    def set_default_project_id(self, project_id: str):
        self.__DEFAULT_PROJECT_ID = project_id

    def get_jql(self) -> dict:
        query_handler = QueryHandler(self.get_default_project_id())
        return query_handler.get_jql()

    def basic_get_response(self, url: str) -> Response:
        BEARER_TOKEN = f'Bearer {self.__APP_TOKEN}'
        headers = {"Accept": "application/json"}

        # On Premise Authentication
        if self.__JIRA_DEFAULT_SERVER_TYPE == self.__JIRA_SERVER_TYPE.on_premise:
            headers = {"Accept": "application/json",
                       "Authorization": BEARER_TOKEN}
            return requests.request("GET", url, headers=headers)

        return requests.request("GET", url, headers=headers, auth=self.__AUTH)
