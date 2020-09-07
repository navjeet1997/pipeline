pipeline {
    agent {
        any { image 'python:3' }
    }
    stages {
        stage('build') {
            steps {
             sh """
    . .env/bin/activate
    pip3 install -r requirement.txt
    """
            }
        }
    }
}



