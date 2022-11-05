// Jenkinsfile (Declarative Pipeline)
/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'python --version'
                bat 'python task01.py'
            }
        }
    }
}