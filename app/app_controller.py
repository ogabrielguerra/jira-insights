from app.JiraInsights.service.core_service import CoreService
from app.JiraInsights.service.api_service import ApiService
from app.JiraInsights.service.data_service import DataService
from app.JiraInsights.service.syncing_service import SyncingService
from app.JiraInsights.service.healthcheck import Healthcheck
from app.JiraInsights.utils import Utils

from fastapi import Request
from fastapi.responses import HTMLResponse

class AppController:

    def __init__(self, app_instance, app_metadata):
        
        self.__CORE_SERVICE = CoreService()
        self.__API_SERVICE = ApiService(self.__CORE_SERVICE)
        self.__DATA_SERVICE = DataService()
        self.__SYNCING_SERVICE = SyncingService(
            self.__CORE_SERVICE, 
            self.__API_SERVICE,
            self.__DATA_SERVICE)
        
        #SYNCING OPERATIONS
        @app_instance.put("/jira/project/load", status_code=201, tags=["Syncing Data"])
        def load_initial_data():
            return self.__SYNCING_SERVICE.initial_load()

        @app_instance.put('/jira/project/sync', status_code=201, tags=["Syncing Data"])
        def sync_project_metadata():
            project_data = [self.__API_SERVICE.get_project_by_id()]
            result = self.__DATA_SERVICE.upsert_project(project_data)
            return Utils.pymongo_result_to_json('upsert_multiple', result)

        @app_instance.put('/jira/project/issue/sync', status_code=201, tags=["Syncing Data"])
        def sync_project_issues():
            issue_data = self.__API_SERVICE.get_issues_by_sprint()
            result = self.__DATA_SERVICE.upsert_issues(issue_data)
            return Utils.pymongo_result_to_json('upsert_multiple', result)

        # CHECKING
        @app_instance.get("/healthcheck", tags=["Maintenance"])
        def health_check():
            return {"Project": app_metadata.app_title}

        @app_instance.post("/healthcheck/insert", tags=["Maintenance"])
        def checks_insert_feature():
            health_check = Healthcheck()
            result = health_check.insert()
            return Utils.pymongo_result_to_json('insert_one', result)

        @app_instance.get("/troubleshoot", tags=["Maintenance"])
        def troubleshooting_info():
            return {"Project": '@TODO: show technical info for troubleshooting.'}


        # QUERYING
        @app_instance.get("/jira/project", tags=["Querying Jira"])
        def get_project_metadata_from_jira_server():
            return self.__API_SERVICE.get_project_by_id()

        @app_instance.get("/jira/project/issue/count", tags=["Querying Jira"])
        def get_project():
            return self.__API_SERVICE.get_project_total_issues()

        @app_instance.get("/jira/project/current-sprint", tags=["Querying Jira"])
        def get_current_sprint():
            return self.__API_SERVICE.get_current_sprint()
