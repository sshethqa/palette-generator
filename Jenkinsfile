pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "bash scripts/install.sh"
            }
        }
        stage('Test') {
            steps {
                sh "bash scripts/test.sh"
            }
        }
        stage('Deploy') {
            steps {
                sh "python3 app.py"
                sh "bash scripts/deploy.sh"
            }
        }
    }
}