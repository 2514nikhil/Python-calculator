pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t calculator-service .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh 'docker run --rm calculator-service'
            }
        }
    }

    post {
        success {
            echo 'Docker Pipeline Success!'
        }
        failure {
            echo 'Docker Pipeline Failed!'
        }
    }
}
