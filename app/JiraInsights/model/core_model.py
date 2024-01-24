from os import environ
from pymongo import MongoClient
from app.JiraInsights.service.logging_service import LoggingService
import urllib
from fastapi import HTTPException

class CoreModel:

    def __init__(self):
        self.__CONNECTION = None
        self.__DEFAULT_DATABASE = environ['MONGO_DATABASE']

    def raise_422_exception(self, reference: str, exception_error_message):
        full_error_message = reference + ' | ' + str(exception_error_message)
        LoggingService('error', full_error_message)
        raise HTTPException(status_code=422, detail=full_error_message)

    def get_db_client_connection(self, recreate: bool=False) -> MongoClient:
        
        HOST = environ['MONGO_HOST']
        USERNAME = urllib.parse.quote_plus(environ['MONGO_USERNAME'])
        PASSWORD = urllib.parse.quote_plus(environ['MONGO_PASSWORD'])
        CONNECTION_STRING = 'mongodb://%s:%s@%s/?authMechanism=SCRAM-SHA-1' % (
            USERNAME, PASSWORD, HOST)

        if not self.__CONNECTION or recreate:
            try:
                client = MongoClient(CONNECTION_STRING)
                self.__CONNECTION = client[self.__DEFAULT_DATABASE]
            except Exception as e:
                self.raise_422_exception('get_db_client_connection', e)

        return self.__CONNECTION

    def get_data_by_query(self, collection_reference, query):
        connection = self.get_db_client_connection()
        mongo_collection = connection[collection_reference]
        return mongo_collection.find(query)
        

    def get_mongo_collection_reference(self, collection_reference):
        connection = self.get_db_client_connection()
        return connection[collection_reference]


    def get_data_by_query(self, collection_reference, query) -> dict:
        mongo_collection = self.get_mongo_collection_reference(collection_reference)
        return mongo_collection.find(query)
        

    def insert_one(self, document, collection_reference: str):
        mongo_collection = self.get_mongo_collection_reference(collection_reference)

        try:
            result = mongo_collection.insert_one(document)
            return result

        except Exception as e:
            self.raise_422_exception('insert_one', e)


    def insert_many(self, issue_documents: dict, collection_reference:str) -> object:
        mongo_collection = self.get_mongo_collection_reference(
            collection_reference)

        try:
            result = mongo_collection.insert_many(issue_documents)
            return result

        except Exception as e:
            self.raise_422_exception('insert_many', e)


    def upsert_many(self, document_collections: dict, collection_reference: str) -> list:
        
        mongo_collection = self.get_mongo_collection_reference(
            collection_reference)

        upserted_ids = []
        DOCUMENT_KEY = 'id'

        try:
            for document in document_collections:
                document_id = str(document.get('id'))
                
                result = mongo_collection.replace_one(
                    {DOCUMENT_KEY: document_id},
                    document, 
                    upsert=True
                )
                
                upserted_ids.append(str(result.upserted_id))
            
            return upserted_ids
        
        except Exception as e:
            self.raise_422_exception('upsert_many', e)


    def drop_collection(self, collection_reference:str) -> bool:
        mongo_collection = self.get_mongo_collection_reference(
            collection_reference)

        try:
            mongo_collection.drop()
            return True

        except Exception as e:
            self.raise_422_exception('drop_collection', e)
