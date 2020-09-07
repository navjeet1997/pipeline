pipeline {
    agent {
        any { image 'python:3' }
    }
    stages {
        stage('build') {
            steps {
                withEnv(['PATH+EXTRA=/usr/local/bin']) {  
          	sh 'which python3' 
        	}
            }
        }
    }
}



