
# JIRA INSIGHTS
Jira Insights is a REST API service which extracts data from a Jira server and then save it into a Mongo database (ETL - Extract, transform, load).

## WHY?
Though Jira is comonly found being the Agile workhorse througout companies, it's also commom to face several performance issues, due to it's design and implementation. 

However, Jira is a rich source for managers, Product Owners and Scrum Masters and makes no sense being prevented from using that information because of resources consumption limitations. 

The answer for this question is to apply ETL concepts, extracting data from the Jira server, transforming it properly and then storing it in a Mongo database, ready to be queried at anytime.

One important key aspect is querying Jira directly we can get realtime information. To mitigate this problem, we use a Syncing Service which loads **only the delta**, leveraging MongoDB upsert feature. It can be configure to be called multiple times and in a convenient frequency, depending on the company use and needs.

## API DOCUMENTATION
You can find a Swagger here:
[server_url]/documentation

## USAGE

## Start application
Head to application root directory and run:

```
docker-compose up -d
```

## Extracting data
For available endpoints, please refer to the Swagger documentation.

## Reading logs:
```
docker-compose logs -f --tail=100 jde-api-service
```

## Entering container:
```
docker exec -it jde-api-service /bin/bash
```

## Run tests
```
docker exec -it jde-api-service sh app/run-tests.sh
```
