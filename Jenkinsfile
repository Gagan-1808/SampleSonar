pipeline {
    agent any


    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Gagan-1808/SampleSonar.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                   
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests with Coverage') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m coverage run -m pytest
                    python -m coverage report
                    python -m coverage xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                    withSonarQubeEnv('sonarqube') {   // name must match Jenkins → System config
                        withCredentials([string(credentialsId: 'SonarqubeProj', variable: 'SonarqubeProj')]) {
                            sh '''
                                sonar-scanner \
                                 -Dsonar.token=${SonarqubeProj}
                            '''
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
           stage('Notify – Quality Gate Passed') {
            steps {
                mail(
                    to: "gagan.patwal.1@gmail.com",
                    subject: "✅ Sample Python Project - SonarQube Quality Gate Passed – Build #${env.BUILD_NUMBER}",
                    body: """
Hi,

Good news! The SonarQube Quality Gate has PASSED for the latest build.

──────────────────────────────────────────
Project     : "Sample Python Project"
Branch      : main
Build #     : ${env.BUILD_NUMBER}
Build URL   : ${env.BUILD_URL}
Repository  : ${env.GITHUB_PR_URL}
──────────────────────────────────────────

All checks have passed:
  ✅ Tests with Coverage – PASSED
  ✅ SonarQube Analysis  – PASSED
  ✅ Quality Gate        – PASSED

The code is clean and ready for review.

Regards,
Jenkins CI
                    """
                )
            }
        }
    }
    

    post {
        always {
            echo 'Cleaning workspace...'
            cleanWs()
        }

        success {
            echo 'Pipeline SUCCESS 🚀'
        }

        failure {
            echo 'Pipeline FAILED ❌'
        }
    }
}
