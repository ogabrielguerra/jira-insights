import random
from faker import Faker

class DatabaseMock:

    @staticmethod
    def create_issue_mock(params:dict):
        issue_mock = IssueMock()
        obj = issue_mock.get_issue_mock()
        obj.update(id = params.get('id'))
        obj.update(key = params.get('key'))
        obj.update(self='https://fake/rest/api/2/'+str(params.get('id')))
        
        return obj


    def __init__(self):
        self.fake = Faker()
        self.objs = []


    def issue_mock_builder(self, num_items:int):
        
        for i in range(num_items):
            issue_id = random.randint(0, 30000)
            key = 'POC-'+str(issue_id)
            
            params = {
                'id': issue_id,
                'key': key
            }

            self.objs.append(DatabaseMock.create_issue_mock(params))


    def get_issues_list(self):
        return self.objs


class IssueMock:

    def __init__(self):
        self.__issue = {
            "id": None,
            "self": None,
            "key": None,
            "fields": {
                "statuscategorychangedate": "2021-11-26T12:16:32.017-0300",
                "issuetype": {
                    "self": "https://gabrielguerra.atlassian.net/rest/api/2/issuetype/10001",
                    "id": "10001",
                    "description": "Functionality or a feature expressed as a user goal.",
                    "iconUrl": "https://gabrielguerra.atlassian.net/secure/viewavatar?size=medium&avatarId=10315&avatarType=issuetype",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": 3.0,
                "project": {
                    "self": "https://gabrielguerra.atlassian.net/rest/api/2/project/10000",
                    "id": "10000",
                    "key": "POC",
                    "name": "pocdemo",
                    "projectTypeKey": "software",
                    "simplified": False,
                    "avatarUrls": {
                        "48x48": "https://gabrielguerra.atlassian.net/secure/projectavatar?pid=10000&avatarId=10411",
                        "24x24": "https://gabrielguerra.atlassian.net/secure/projectavatar?size=small&s=small&pid=10000&avatarId=10411",
                        "16x16": "https://gabrielguerra.atlassian.net/secure/projectavatar?size=xsmall&s=xsmall&pid=10000&avatarId=10411",
                        "32x32": "https://gabrielguerra.atlassian.net/secure/projectavatar?size=medium&s=medium&pid=10000&avatarId=10411"
                    }
                },
                "customfield_10033": None,
                "fixVersions": [],
                "aggregatetimespent": None,
                "customfield_10034": None,
                "resolution": None,
                "customfield_10035": None,
                "customfield_10036": None,
                "customfield_10037": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "watches": {
                    "self": "https://gabrielguerra.atlassian.net/rest/api/2/issue/POC-6/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "lastViewed": "2021-11-26T12:17:12.687-0300",
                "created": "2021-11-26T12:16:31.835-0300",
                "customfield_10020": [
                    {
                        "id": 2,
                        "name": "POC Sprint 2",
                        "state": "active",
                        "boardId": 1,
                        "goal": "",
                        "startDate": "2021-11-26T15:17:34.567Z",
                        "endDate": "2021-12-03T20:48:00.000Z"
                    }
                ],
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://gabrielguerra.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://gabrielguerra.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": [],
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0002n:",
                "aggregatetimeoriginalestimate": None,
                "timeestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2021-11-26T12:17:12.604-0300",
                "status": {
                    "self": "https://gabrielguerra.atlassian.net/rest/api/2/status/10000",
                    "description": "",
                    "iconUrl": "https://gabrielguerra.atlassian.net/",
                    "name": "To Do",
                    "id": "10000",
                    "statusCategory": {
                        "self": "https://gabrielguerra.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "Another test",
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "security": None,
                "customfield_10007": None,
                "customfield_10008": None,
                "aggregatetimeestimate": None,
                "customfield_10009": None,
                "summary": "Another test",
                "creator": {
                    "self": "https://gabrielguerra.atlassian.net/rest/api/2/user?accountId=557058%3A0700a6cf-37a3-4814-8dd1-3a460586625b",
                    "accountId": "557058:0700a6cf-37a3-4814-8dd1-3a460586625b",
                    "emailAddress": "gabrielguerra@gmail.com",
                    "avatarUrls": {
                        "48x48": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:0700a6cf-37a3-4814-8dd1-3a460586625b/7892ed8e-926b-4b9d-b9ce-934b74570fef/48",
                        "24x24": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:0700a6cf-37a3-4814-8dd1-3a460586625b/7892ed8e-926b-4b9d-b9ce-934b74570fef/24",
                        "16x16": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:0700a6cf-37a3-4814-8dd1-3a460586625b/7892ed8e-926b-4b9d-b9ce-934b74570fef/16",
                        "32x32": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:0700a6cf-37a3-4814-8dd1-3a460586625b/7892ed8e-926b-4b9d-b9ce-934b74570fef/32"
                    },
                    "displayName": "Gabriel Guerra",
                    "active": True,
                    "timeZone": "America/Sao_Paulo",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://gabrielguerra.atlassian.net/rest/api/2/user?accountId=557058%3A0700a6cf-37a3-4814-8dd1-3a460586625b",
                    "accountId": "557058:0700a6cf-37a3-4814-8dd1-3a460586625b",
                    "emailAddress": "gabrielguerra@gmail.com",
                    "avatarUrls": {
                        "48x48": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:0700a6cf-37a3-4814-8dd1-3a460586625b/7892ed8e-926b-4b9d-b9ce-934b74570fef/48",
                        "24x24": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:0700a6cf-37a3-4814-8dd1-3a460586625b/7892ed8e-926b-4b9d-b9ce-934b74570fef/24",
                        "16x16": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:0700a6cf-37a3-4814-8dd1-3a460586625b/7892ed8e-926b-4b9d-b9ce-934b74570fef/16",
                        "32x32": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:0700a6cf-37a3-4814-8dd1-3a460586625b/7892ed8e-926b-4b9d-b9ce-934b74570fef/32"
                    },
                    "displayName": "Gabriel Guerra",
                    "active": True,
                    "timeZone": "America/Sao_Paulo",
                    "accountType": "atlassian"
                },
                "customfield_10000": "{}",
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "customfield_10039": [],
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://gabrielguerra.atlassian.net/rest/api/2/issue/POC-6/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        }


    def get_issue_mock(self):
        return self.__issue    
