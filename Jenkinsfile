// Jenkinsfile

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Install dependencies, if any
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run Selenium tests
                    sh 'python -m unittest tests.test_calculator'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Build and deploy the Docker container
                    sh 'docker build -t calculator-app .'
                    sh 'docker run -d -p 5000:5000 --name calculator-container calculator-app'
                }
            }
        }
    }
}

