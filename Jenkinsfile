pipeline {
    agent { any { image 'python:3.5.1' } }
    stages {
    stage('build') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
        stage('Test'){
            steps {
                sh "python main.py"
            }
        }
    }
   
 }
