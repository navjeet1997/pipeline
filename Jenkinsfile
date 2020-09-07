pipeline {
    agent {
        any { image 'python:3.8' }
    }
    stages {
        stage('build') {
            steps {
                script{
                    withPythonEnv('/usr/local/bin/python3.8') {
	
	                sh 'pip3 install -r requirements.txt'
                    }
                }
            }
        }
    }
}



