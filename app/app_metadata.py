class AppMetadata:

    app_title = 'Jira Insights'
    
    metadata = {
        'app_title' : app_title,
        'tags_metadata' : [
            {
                "name": "Maintenance",
                "description": "Checking application health and availability.",
            },
            {
                "name": "Syncing Data",
                "description": "Syncing project and issues data between Jira and MongoDB.",
            },
            {
                "name": "Querying Jira",
                "description": "Querying Jira server.",
            },
        ]
    }

    tags_metadata = metadata.get('tags_metadata')
    
    description = 'This application extracts data from Jira and stores it in a MongoDB database for further processing.'
    version = '0.0.1'
    contact_name = 'Gabriel Guerra'
    contact_url = 'gabrielguerra.me'
    contact_email = 'gabrielguerra@gmail.com'
