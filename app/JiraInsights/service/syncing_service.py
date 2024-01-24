import math
from app.JiraInsights.service.logging_service import LoggingService
from fastapi import HTTPException

class SyncingService:
    
    def __init__(self, core_service, api_service, data_service) -> None:
        self.__API_SERVICE = api_service
        self.__DATA_SERVICE = data_service
        self.__JQL_QUERIES: dict = core_service.get_jql()
        self.__COUNT_PROJECT_ISSUES: str = self.__JQL_QUERIES.get(
            'project_total_issues')
        self.__ALL_PROJECT_ITEMS: str = self.__JQL_QUERIES.get(
            'all_project_items')


    def get_project_total_issues(self) -> dict:
        data = self.__API_SERVICE.get_project_issue_by_jql(
            self.__COUNT_PROJECT_ISSUES, only_issues=False)
        LoggingService('info', 'Succesfully retrieved number of total issues')
        return {'total': data.get('total')}


    def get_issue_data_by_chunks(self, total_issues):
        ISSUES_PER_ITERATION = 200
        TOTAL_REQUESTS = math.ceil(total_issues / ISSUES_PER_ITERATION)

        start_at = 0
        issues = []
        iteration_index = 1

        for _ in range(TOTAL_REQUESTS):
            try:
                issue_data = self.__API_SERVICE.get_project_issue_by_jql(
                    jql_filter=self.__ALL_PROJECT_ITEMS,
                    start_at=start_at,
                    max_results=ISSUES_PER_ITERATION)
                issues.append(issue_data)
                start_at += ISSUES_PER_ITERATION

            except Exception as e:
                error_message = 'Getting issues failed at #' + \
                    str(iteration_index) + ' iteration. ' + str(e)
                LoggingService('error', error_message)
                raise HTTPException(
                    status_code=422, detail=error_message)

            iteration_index += 1

        return issues


    def save_issues(self, bulk_issues):
        try:
            for i in range(len(bulk_issues)):
                self.__DATA_SERVICE.upsert_issues(bulk_issues[i])
        except Exception as e:
            error_message = 'Saving to database failed | ' + str(e)
            LoggingService('error', error_message)
            raise HTTPException(status_code=422, detail=error_message)


    def initial_load(self, drop_collection=False):
        total_issues = self.get_project_total_issues()
        total_issues = total_issues.get('total')

        # Drop the collection if necessary
        if drop_collection:
            self.__DATA_SERVICE.drop_collection('issue')

        # Get issues data from Jira Server
        issues = self.get_issue_data_by_chunks(total_issues)

        # Save issues to Mongo Database
        self.save_issues(issues)

        # Success
        LoggingService('info', 'Succesfully loaded all project issues.')
        return {"status": "success"}
