
class Settings():

    def __init___(self):
        self.repositories = {
            'postgres': {
                'host': 'localhost', 
                'port': 2000, 
                'password': ''
            }
        }

        self.api = {
            'host': '0.0.0.0', 
            'port': 6666
        } 


    def get_job_config(self, job_name, cvs_url, pipeline):
        # return """<?xml version='1.1' encoding='UTF-8'?>
        #     <project>
        #     <builders>
        #         <hudson.tasks.Shell>
        #         <command>echo $JENKINS_VERSION</command>
        #         </hudson.tasks.Shell>
        #     </builders>
        #     </project>"""
        return '''
            <flow-definition plugin="workflow-job@2.41">
            <description> holaaa </description>
            <keepDependencies>false</keepDependencies>
            <properties>
            <com.coravy.hudson.plugins.github.GithubProjectProperty plugin="github@1.34.1">
            <projectUrl> https://github.com/pedbermar/wellness_challenge </projectUrl>
            <displayName/>
            </com.coravy.hudson.plugins.github.GithubProjectProperty>
            </properties>
            <definition class="org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition" plugin="workflow-cps@2.94">
                <script>
pipeline { 
    agent { dockerfile true } 
    stages { 
        stage('Test') { 
            steps { 
                sh 'node --version' 
                sh 'svn --version' 
            } 
        } 
    } 
} 
</script>
                <sandbox>true</sandbox>
            </definition>
            <triggers/>
            <authToken>z</authToken>
            <disabled>false</disabled>
            </flow-definition>
            
            '''