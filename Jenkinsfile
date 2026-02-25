pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Detect Docker') {
            steps {
                script {
                    env.HAS_DOCKER = (sh(script: 'command -v docker >/dev/null 2>&1', returnStatus: true) == 0) ? 'true' : 'false'
                    echo "Docker available: ${env.HAS_DOCKER}"
                }
            }
        }

        stage('Build Docker Image') {
            when {
                expression { env.HAS_DOCKER == 'true' }
            }
            steps {
                sh 'docker build -t calculator-service .'
            }
        }

        stage('Run Tests in Docker') {
            when {
                expression { env.HAS_DOCKER == 'true' }
            }
            steps {
                sh 'docker run --rm calculator-service'
            }
        }

        stage('Run Tests without Docker') {
            when {
                expression { env.HAS_DOCKER != 'true' }
            }
            steps {
                sh '''
                    set -e
                    if command -v python3 >/dev/null 2>&1; then
                      PY_CMD=python3
                    elif command -v python >/dev/null 2>&1; then
                      PY_CMD=python
                    else
                      echo "Python is not installed on this Jenkins agent."
                      exit 1
                    fi

                    $PY_CMD -m pip install --upgrade pip
                    $PY_CMD -m pip install -r requirements.txt
                    $PY_CMD -m pytest -v
                '''
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
