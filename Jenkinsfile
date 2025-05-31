pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    if (fileExists('requirements.txt')) {
                        bat 'pip install -r requirements.txt'
                    } else {
                        echo 'No requirements.txt found, skipping pip install'
                    }
                }
            }
        }
        stage('Run Python Code') {
            steps {
                script {
                    if (fileExists('main.py')) {
                        bat 'python main.py'
                    } else {
                        echo 'main.py not found, skipping execution'
                    }
                }
            }
        }
    }
    post {
        failure {
            echo "Pipeline failed on branch: ${env.BRANCH_NAME}"
        }
    }
}
