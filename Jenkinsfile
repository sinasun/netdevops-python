pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t network-monitoring-app:latest .'
                sh 'docker push network-monitoring-app:latest'
            }
        }
        
        stage('Testing') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest'
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f network-monitoring-deployment.yaml'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
