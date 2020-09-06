pipeline {
    agent { any { image 'python:3.5.1' } }
    stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stages {
        stage('Test'){
            steps {
                sh "python main.py"
            }
        }
    }
   
 }
