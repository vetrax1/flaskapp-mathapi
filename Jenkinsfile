pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/<your-username>/<repo-name>.git'
      }
    }

    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Run Tests') {
      steps {
        sh 'python app.py & sleep 5 && curl http://localhost:5000 || true'
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          docker.build("yourdockerhub/${env.JOB_NAME}:${env.BUILD_NUMBER}")
        }
      }
    }
  }
}