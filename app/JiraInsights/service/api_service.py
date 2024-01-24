import json
import math
from app.JiraInsights.service.logging_service import LoggingService
from fastapi import HTTPException
class ApiService:

    def __init__(self, core_service: object) -> None:

        self.__CORE_SERVICE = core_service
        self.__BASE_URL :str = core_service.get_base_url()
        self.__PROJECT_ID :str = core_service.get_default_project_id()
        self.__JQL_QUERIES :dict = core_service.get_jql()
        self.__JQL_ISSUES_BY_SPRINT: str = self.__JQL_QUERIES.get(
            'issues_by_sprint')
        self.__JQL_CURRENT_SPRINT: str = self.__JQL_QUERIES.get(
            'current_sprint')
        self.__COUNT_PROJECT_ISSUES: str = self.__JQL_QUERIES.get('project_total_issues')

    def get_project_by_id(self, project_id: str=None) -> json:
        
        url:str = self.__BASE_URL + 'project/'+self.__PROJECT_ID
        if project_id:
            url = self.__BASE_URL + 'project/'+project_id

        try:
            response = self.__CORE_SERVICE.basic_get_response(url)
            LoggingService('info', 'Succesfully retrieved Jira data from ' + url)
            return json.loads(response.text)
        
        except Exception as e:
            LoggingService('error', 'Impossible to retrieve Jira data. ' + str(e))
            return None
    
    def get_project_total_issues(self) -> dict:
        data = self.get_project_issue_by_jql(
            self.__COUNT_PROJECT_ISSUES, only_issues=False)
        LoggingService('info', 'Succesfully retrieved number of total issues')
        return {'total': data.get('total')}


    def get_issues_by_sprint(self) -> dict:
        current_sprint = self.get_current_sprint()
        current_sprint = current_sprint.get('current_sprint')

        return self.get_project_issue_by_jql(self.__JQL_ISSUES_BY_SPRINT+current_sprint)


    def get_current_sprint(self):
        current_sprint = self.get_project_issue_by_jql(self.__JQL_CURRENT_SPRINT, start_at=0, max_results=1)
        current_sprint = current_sprint[0].get('fields').get('customfield_10005')[0]
        current_sprint = current_sprint.split('name=')
        current_sprint = current_sprint[1].split(',')
        return {'current_sprint': current_sprint[0]}


    def get_project_issue_by_jql(self, jql_filter:str, start_at:int=0, max_results:int=50, only_issues:bool=True) -> dict:
        
        full_filter = self.__BASE_URL+jql_filter + '&startAt=' + str(start_at)+'&maxResults=' + str(max_results)
        response = self.__CORE_SERVICE.basic_get_response(full_filter)
        issue_data = json.loads(response.text)
        
        if only_issues:
            return issue_data.get('issues')

        return issue_data


    

