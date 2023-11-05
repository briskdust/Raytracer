pipeline {
  agent any
  stages {
    stage('List Files') {
      steps {
        sh 'ls -la'
      }
    }

    stage('') {
      steps {
        sh 'docker build .'
      }
    }

  }
}