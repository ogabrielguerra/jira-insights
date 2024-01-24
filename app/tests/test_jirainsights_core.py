import unittest
import pymongo
from os import environ

from unittest.mock import patch
from app.JiraInsights.model.core_model import CoreModel
from app.JiraInsights.service.core_service import CoreService
from requests import Response


class TestCore(unittest.TestCase):

    DEFAULT_BASE_URL = environ['JIRA_API_URL']
    HOME_RESPONSE = '{"Project":"Jira Insights"}'
    APP_BASE_URL = 'http://localhost:8000/'
    DEFAULT_PROJECT_ID = 'PROJECT_ID'


    @classmethod
    def setUpClass(self):
        self.__core_service = CoreService()
        self.__core_model = CoreModel()  


    def test_get_base_url(self):        
        base_url = self.__core_service.get_base_url()
        self.assertTrue(isinstance(base_url, str))
        self.assertEqual(base_url, self.DEFAULT_BASE_URL)


    def test_get_default_project_id(self):
        project_id = self.__core_service.get_default_project_id()
        self.assertEqual(project_id, self.DEFAULT_PROJECT_ID)


    def test_get_jql(self):
        jql = self.__core_service.get_jql()
        self.assertTrue(isinstance(jql,dict))


    def test_basic_get_response(self):
        response = self.__core_service.basic_get_response(
            self.APP_BASE_URL+'healthcheck/')
        
        self.assertTrue(isinstance(response, Response))
        self.assertEqual(response.text, self.HOME_RESPONSE)

        url_jira_api_project = self.DEFAULT_BASE_URL + 'jira/project/'
        response = self.__core_service.basic_get_response(url_jira_api_project)
        self.assertTrue(isinstance(response, Response))


    def test_get_db_client_connection(self):
        db_connection = self.__core_model.get_db_client_connection()
        self.assertTrue(isinstance(db_connection, pymongo.database.Database))       
    
