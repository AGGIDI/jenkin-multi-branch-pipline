pipeline {
    agent any

    environment {
        // Optional: Add virtual environment or other env vars here
        PYTHON_SCRIPT = 'main.py'
    }

    stages {
        stage('Clone Repo') {
            steps {
                // Jenkins automatically checks out the current branch
                echo "Checking out branch: ${env.BRANCH_NAME}"
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install pip packages
                    if (fileExists('requirements.txt')) {
                        sh 'pip3 install -r requirements.txt'
                    } else {
                        echo "No requirements.txt found, skipping pip install"
                    }
                }
            }
        }

        stage('Run Python Code') {
            steps {
                script {
                    if (fileExists("${env.PYTHON_SCRIPT}")) {
                        sh "python3 ${env.PYTHON_SCRIPT}"
                    } else {
                        error "Python script ${env.PYTHON_SCRIPT} not found!"
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully on branch: ${env.BRANCH_NAME}"
        }
        failure {
            echo "Pipeline failed on branch: ${env.BRANCH_NAME}"
        }
    }
}
