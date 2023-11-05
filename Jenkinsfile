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

  }
}