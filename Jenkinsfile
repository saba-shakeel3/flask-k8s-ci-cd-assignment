pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f kubernetes/'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl rollout status deployment/flask-app'
                sh 'kubectl get pods'
                sh 'kubectl get services'
            }
        }
    }
}
