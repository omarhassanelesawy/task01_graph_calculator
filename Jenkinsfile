// Jenkinsfile (Declarative Pipeline)
/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('git repo clone') {
            steps {
                git 'https://github.com/omarhaassaan/task01_graph_calculator'
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}