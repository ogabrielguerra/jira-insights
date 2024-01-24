from fastapi import FastAPI
from app.app_metadata import AppMetadata as app_metadata

class AppFactory:
    
    def __init__(self):

        self.__APP = FastAPI(
            docs_url="/documentation", 
            redoc_url=None,
            openapi_tags=app_metadata.tags_metadata,
            title=app_metadata.app_title,
            description=app_metadata.description,
            version=app_metadata.version,
            contact={
                "name": app_metadata.contact_name,
                "url": app_metadata.contact_url
            },
        )
        self.__METADATA = app_metadata
        

    def get_instance(self):
        return self.__APP

    def get_templates(self):
        return self.__TEMPLATES

    def get_metadata(self):
        return self.__METADATA
        
