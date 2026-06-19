pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run API Automation Tests') {
            steps {
                bat 'pytest tests -v'
            }
        }
    }
}