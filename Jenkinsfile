pipeline {
    agent {
        any { image 'python:3' }
    }
    stages {
        stage('buld') {
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



