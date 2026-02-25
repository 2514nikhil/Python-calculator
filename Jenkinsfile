pipeline {
    agent any

    parameters {
        string(name: 'ALERT_EMAIL', defaultValue: '', description: 'Recipient email for failure notifications')
    }

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

                                        $PY_CMD -m venv .venv
                                        . .venv/bin/activate
                                        python -m pip install --upgrade pip
                                        pip install -r requirements.txt
                                        pytest -v
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
            script {
                if (params.ALERT_EMAIL?.trim()) {
                    mail(
                        to: params.ALERT_EMAIL.trim(),
                        subject: "FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                        body: """Job: ${env.JOB_NAME}
Build: #${env.BUILD_NUMBER}
Status: FAILED
Branch: ${env.BRANCH_NAME ?: 'N/A'}
Build URL: ${env.BUILD_URL}
"""
                    )
                } else {
                    echo 'ALERT_EMAIL is empty. Skipping failure email notification.'
                }
            }
        }
    }
}