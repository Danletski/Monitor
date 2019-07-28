Jenkinsfile

pipeline {
	agent any
	stages {
	    stage ('Pull') {
			steps {
				git 'https://github.com/Danletski/Monitor.git'
			}
		}
		stage ('Deploy Vagrant') {
			steps {
				sh 'sudo vagrant up -d'
			}
		}
		stage ('Test') {
			steps {
				sh 'vagrant ssh'
				sh 'cd /etc/ansible/'
			        sh 'sudo chmod +x testSuccess.py'
				sh 'sudo python testSuccess.py'
			}
		}
		stage ('Stop') {
		    steps {
		        sh 'exit'
		        sh 'vagrant destroy -y'
		    }
		}
	}
}
