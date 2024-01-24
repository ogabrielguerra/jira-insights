class QueryHandler:

    def __init__(self, project_id: str):

        DEFAULT_FIELDS = 'project,issuetype,created,updated,status,summary,priority,reporter,assignee,duedate,resolutiondate,timeoriginalestimate,timeestimate,timespent'

        CUSTOM_FIELD_SPRINT = 'customfield_10005' 
        CUSTOM_FIELD_REQUEST_TYPE = 'customfield_12062'
        CUSTOM_FIELD_REQUEST_GROUP = 'customfield_16740'
        CUSTOM_FIELD_TYPE_OF_WORK = 'customfield_16136'
        CUSTOM_FIELD_SCOPE_OF_SERVICE = 'customfield_11612'

        CUSTOM_FIELDS = CUSTOM_FIELD_SPRINT+','+CUSTOM_FIELD_REQUEST_TYPE+','+CUSTOM_FIELD_REQUEST_GROUP+','+CUSTOM_FIELD_TYPE_OF_WORK+','+CUSTOM_FIELD_SCOPE_OF_SERVICE

        PROJECT = 'search?jql=project='+project_id

        QUERY_CREATED_BEFORE_TODAY = PROJECT + ' AND createdDate < startOfDay()'
        QUERY_ALL_PROJECT_ITEMS = PROJECT + '&fields=' + DEFAULT_FIELDS+','+CUSTOM_FIELDS
        QUERY_PROJECT_TOTAL_ISSUES = PROJECT + '&fields=issues'
        QUERY_ISSUES_BY_SPRINT = PROJECT + '&fields=issues AND Sprint='
        QUERY_CURRENT_SPRINT = PROJECT + ' AND resolution=unresolved&fields=' + CUSTOM_FIELD_SPRINT
        
        self.__JQL = {
            'created_before_today': QUERY_CREATED_BEFORE_TODAY,
            'all_project_items': QUERY_ALL_PROJECT_ITEMS,
            'project_total_issues': QUERY_PROJECT_TOTAL_ISSUES,
            'issues_by_sprint': QUERY_ISSUES_BY_SPRINT,
            'current_sprint': QUERY_CURRENT_SPRINT
        }


    def get_jql(self) -> dict:
        return self.__JQL