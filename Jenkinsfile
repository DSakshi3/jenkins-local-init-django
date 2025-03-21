pipeline {
    agent { label 'agent' }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django-example:${BUILD_NUMBER} .'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'docker run --rm django-example:${BUILD_NUMBER} python manage.py test'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'In a production environment, deployment would happen here'
                echo 'For example, pushing to a container registry or deploying to Kubernetes'
            }
        }
    }
    
    post {
        success {
            echo 'Build successful! The Django application is ready for deployment.'
        }
        failure {
            echo 'Build failed! Check the logs for details.'
        }
        always {
            // Clean up Docker images
            sh 'docker rmi django-example:${BUILD_NUMBER} || true'
        }
    }
}