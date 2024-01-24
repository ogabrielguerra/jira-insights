import requests

class SyncService:

    def __init__(self):
        self.headers = {"Accept": "application/json"}
        self.base_url = 'http://172.19.0.2:8000'
        self.healthcheck_url = self.base_url+'/healthcheck'
        self.load_data_url = self.base_url+'/jira/project/load'

        self.attempts = 0
        self.max_attempts = 5
        self.sync_failed = True


    def log_wrapper(self, status: str, message: str) -> None:
        print(f'LOG {status} | {message}')


    def query_service_status(self):
        try:
            response = requests.request("GET", self.healthcheck_url, headers=self.headers)
            if response.status_code != 200:
                self.log_wrapper('ERROR', 'Service unavailable.')
                self.log_wrapper('INFO', str(response.status_code))
            else:
                self.log_wrapper('INFO', 'Service is running.')

        except requests.exceptions.RequestException as error:
            self.log_wrapper('ERROR', error)


    def do_sync(self):
        
        error_message = 'Unable to sync data.'

        try:
            response = requests.request("PUT", self.load_data_url, headers=self.headers)
            
            if response.status_code != 201:
                self.log_wrapper('ERROR', error_message)
                self.sync_failed = True
                self.attempts += 1
            elif response.status_code == 201:
                self.sync_failed = False
            
            self.log_wrapper('INFO', 'Got status code '+ str(response.status_code))

        except requests.exceptions.RequestException as error:
            self.log_wrapper('ERROR', error)


    def max_attempts_not_reached(self):
        return self.attempts <= self.max_attempts


    def run(self):
        self.query_service_status()
        self.log_wrapper('INFO', 'Start syncing...')

        while self.sync_failed and self.max_attempts_not_reached():
            self.log_wrapper('INFO', f'Attempt No {self.attempts} ...')
            self.do_sync()

        if self.sync_failed:
            self.log_wrapper('INFO', 'Sync failed')
        else:
            self.log_wrapper('INFO', 'Sync was successfull.')        


sync = SyncService()
sync.run()