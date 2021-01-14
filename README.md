# Mathapi
A simple microservice that provides the following functionality via RESTful API

## Task
Implement a microservice that exposes an API to solve different mathematical operations: - the pow function - the n-th fibbonaci number - the factorial of the number Use a database to persist all the requests to the API.

Expose the service as an API (not SOAP). Design the service as production ready service.

Nice to haves: containerization, monitoring, caching, authorization, logging via a messaging/streaming framework.

All implementation and design is up to you, following the below restrictions: - use a micro framework (any Flask-like will do, sync or async is up to you) - follow micro services development best practices (MVC/MVCS patterns) - use any API standard except SOAP - consider an implementation that supports extensibility - as the database

layer, use any SQL or NoSQL solution (for simplicity, SQLite will do)
 

Bonus I: Also persist the requests to a message/streaming framework of your choosing.
Bonus II: Implement a cloud native, serverless version of the service (you can implement either one or the other).

## Implemented RESTful API functionality

### Synchronous
* Raise a number to to some power (n^m)
* Find the Nth Fibonacci number
* Find the factorial of a number

### Asynchronous
* Find the Nth Fibonacci number asyncronously and send the result as an email with attached file

# Deployment
The entire application stack could very easily be deployed on a kubernetes cluster by using the provided helm charts and pre-configured values. They are mostly serving for a proof of concept deployment and for demonstrating certain skills rather than for actual production deployment.

## Stack
* Flask, Gunicorn, Nginx - Web app and serving
* PostgreSQL - production RDBMS
* SQLAlchemy - ORM
* Alembic - database migrations
* Docker - app image containerization
* Kubernetes + Helm for orchestrating deployment
* Logstash - log streaming (currently configured only for gunicorn but in future I'll probably make the ingress to stream its logs to elk as well.)
* ELK - log streaming and interface 
* Sentry - Exception logging
* Grafana + Prometheus - monitoring
* Svelte - Minimalistic PoC front-end for the REST API
* Jenkins - CI / CD - configuration as a code with JCASC
* Git - VCS
* Pytest - for test runner
* Black, pre-commit, flake8, isort - pre commit code quality checks
* Poetry - dependency management and virtual environment
## Setup Helm
```
helm dependency update ./helm
helm install --set postgresql.postgresqlPassword=pass --create-namespace --namespace mathapi -f helm/values.yaml -f helm/jenkins_values.yaml mathapi ./helm
```

## Publicly deployed services
The following services are deployed on my personal kubernetes cluster for demonstration purposes:

* Svelte client - https://mathapi.danielpopov.com/
* Sentry - https://mathapi-sentry.danielpopov.com/
* Grafana - https://mathapi-monitoring.danielpopov.com/
* Kibana - https://mathapi-kibana.danielpopov.com/
* Jenkins - https://mathapi-jenkins.danielpopov.com 


# Example Requests

## Compute power (`n`<sup>`x`</sup>) function
```
curl --request POST \
  --url https://mathapi.danielpopov.com/api/v1/exponent \
  --header 'Authorization: Basic xxxxxxxxx' \
  --header 'Content-Type: application/json' \
  --data '{
	"base": 2,
	"exponent": 3
}'
```

## Compute `n`<sup>th</sup> fibonacci number
```
curl --request POST \
  --url https://mathapi.danielpopov.com/api/v1/fibonacci \
  --header 'Authorization: Basic xxxxxxxxx' \
  --header 'Content-Type: application/json' \
  --data '{
	"number": 10
}'
```

## Compute `n!` function
```
curl --request POST \
  --url https://mathapi.danielpopov.com/api/v1/factorial \
  --header 'Authorization: Basic xxxxxxxxx' \
  --header 'Content-Type: application/json' \
  --data '{
	"number": 5
}'
```
## Compute `n`<sup>th</sup> fibonacci number and receive the result via email
```
curl --request POST \
  --url https://mathapi.danielpopov.com/api/v1/fibonacci_async \
  --header 'Authorization: Basic xxxxxxxxx' \
  --header 'Content-Type: application/json' \
  --data '{
"number": 123984,
"email": "lakiyik372@maksap.com"
}'
```