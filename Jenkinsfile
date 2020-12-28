pipeline {
  agent {
    kubernetes {
      yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    pipeline: deploy
spec:
  containers:
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug-v0.17.1
    command: ["cat"]
    imagePullPolicy: Always
    tty: true
  - name: kubectl
    image: strongholder/drone-kubectl
    command: ["cat"]
    imagePullPolicy: Always
    tty: true
"""
    }
  }
  stages {
    stage('Deploy') {
      steps {
        container('kaniko') {
            sh '/kaniko/executor -f `pwd`/Dockerfile -c `pwd` --insecure --skip-tls-verify --whitelist-var-run --cache=true --destination=registry.container-registry:5000/mathapi:latest'
        }
        container('kubectl') {
            withKubeConfig([credentialsId: 'jenkins-robot-kube', serverUrl: 'https://kubernetes.default']) {
              sh 'kubectl delete -f deploy/migrate-job.yaml || true' 
              sh 'kubectl apply -f deploy/migrate-job.yaml'
              sh 'kubectl wait --for=condition=complete job/mathapi-migrate -n mathapi'
              sh 'kubectl rollout restart deployment/mathapi-python -n mathapi'
            }
        }
      }
    }
  }
}
