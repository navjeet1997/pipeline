
pipeline {
    agent { any { image 'python:3.5.1' } }
    stages {
        stage('Test'){
            steps {
                sh "python main.py"
            }
        }
    }
    post {
        always{
            xunit (
                thresholds: [ skipped(failureThreshold: '0'), failed(failureThreshold: '0') ],
                tools: [
                    JUnit(pattern: '**/surefire-reports/*.xml'),
                    JUnit(pattern: '**/generatedJUnitFiles/JUnit/*.xml'),
                    BoostTest(pattern: '**/*_results.xml')]
            )
        }
    }
 }
