pipeline {
    agent {
        any { image 'python:3' }
    }
    stages {
        stage('build') {
            steps {
                script{
                    withPythonEnv('python') {
	
	                sh 'pip3 install -r requirements.txt'
                    }
                }
            }
        }
    }
}



