pipeline {
    agent any
    environment {
        NEXUS_VERSION = "nexus3"
        NEXUS_PROTOCOL = "http"
        NEXUS_URL = "52.20.98.227:8081"
        NEXUS_REPOSITORY = "arkcase"
        NEXUS_CREDENTIAL_ID = "d32ecf61-ba48-4d0f-9bb5-728e8ed16da6"
        NEXUS_NPM_REPOSITORY = "arkcase-npm"
    }
    stages {
        stage("NPM install"){
            
                steps {
                nodejs(nodeJSInstallationName: 'Nodejs16') {
                    sh 'npm install'
                }
            }
        }
        stage("Publish to NPM repository") {
            steps {
                 nodejs(nodeJSInstallationName: 'Nodejs16') {
                        sh '''
                        npm config set registry="http://52.20.98.227:8081/repository/arkcase-npm"
                        npm config set _auth="$(echo -n 'admin:admin@123' | base64)"
                        npm publish
                        '''
                    }
                }
            }
        }
            
}
