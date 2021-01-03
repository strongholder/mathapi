# Mathapi
A simple microservice that provides the following functionality via RESTful API

* Raise a number to to some power (n^m)
* Find the Nth Fibbonaci number
* Find the factorial of a number

# Deployment

# Setup Helm
```
helm dependency update ./helm
helm install --set postgresql.postgresqlPassword=pass --create-namespace --namespace mathapi -f helm/values.yaml -f helm/jenkins_values.yaml mathapi ./helm

```


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