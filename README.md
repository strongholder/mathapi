# Mathapi
A simple microservice that provides the following functionality via RESTful API

* Raise a number to to some power (n^m)
* Find the Nth Fibbonaci number
* Find the factorial of a number

# Deployment

# Setup Helm
```
helm dependency update ./helm
helm install --create-namespace --namespace mathapi -f helm/values.yaml mathapi ./helm

```
