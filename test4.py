from diagrams import Cluster, Diagram
from diagrams.c4 import SystemBoundary, Container
from diagrams.custom import Custom
from diagrams.aws.general import User
from diagrams.aws.devtools import Codecommit
from diagrams.onprem.vcs import Git
from diagrams.aws.devtools import Codebuild
from diagrams.aws.devtools import Codedeploy
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.security import SecurityHub
from diagrams.aws.integration import SNS
from diagrams.aws.management import Cloudwatch
from diagrams.aws.engagement import SimpleEmailServiceSesEmail
from diagrams.aws.compute import EB

graph_attr = {
    "splines": "ortho",
    
}

with Diagram("anh", show=False, graph_attr=graph_attr):
    user1 = User("domain/dev/user")
    mail = SimpleEmailServiceSesEmail("Email")
    sns = SNS("AWS SNS")
    cloudw = Cloudwatch("AWS cloudwatch events")
    cloudw1 = Cloudwatch("AWS cloudwatch logs")
    with SystemBoundary("tool"):
        b = [
        Container(
            name="Dependency Check",
            technology="SCA"
        ),
        Custom("SonarQube", "sona.png")]
    MA = Container(
        name="Manual Approval"
    )
    
    with SystemBoundary("AWS codepipeline"):
        git = Git("Git")
        commit = Codecommit("AWS code commit")
        buil = Codebuild("AWS code build")
        deploy = Codedeploy("AWS code deploy")
        buil1 = Codebuild("AWS code build test")
        deploy1 = Codedeploy("AWS code deploy")
        a = [git >> commit >> buil >> deploy >> buil1 >> deploy1]
    user = User("dev / user")
    elas = EB("AWS elastic (Staging)")
    elas1 = EB("AWS elastic (Production)")
    s3 = S3("AWS S3")
    lamd = Lambda("AWS Lambda")
    secuhub = SecurityHub("AWS securityhub")
    OW = Container(
        name="OWASP (DAST)"
    )
    
     
    user >> a
    buil >> lamd >> secuhub
    buil >> s3 << lamd
    buil1 >> OW
    deploy >> elas
    deploy1 >> elas1
    buil >> b
    a >> sns
    a >> cloudw
    a >> cloudw1
    user1 << mail << sns << cloudw
