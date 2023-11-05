pipeline {
  agent any
  stages {
    stage('List Files') {
      steps {
        sh 'ls -la'
      }
    }

    stage('Build Image') {
      steps {
        sh 'docker build . -t briskdust/raytracer:latest'
      }
    }

    stage('Login to Dockerhub') {
      environment {
        USERNAME = 'briskdust'
        PASSWORD = 'Torso0147'
      }
      steps {
        sh 'docker login -u $USERNAME -p $PASSWORD'
      }
    }

    stage('Push') {
      steps {
        sh 'docker push briskdust/raytracer:latest'
      }
    }

  }
}