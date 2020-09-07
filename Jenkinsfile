pipeline {
    agent {
        any { image 'python:3' }
    }
    stages {
        stage('build') {
            steps {
             withEnv(['Ra=/usr/bin']) {  
          	sh 'which $Ra/python' 
        	}
            }
        }
    }
}



