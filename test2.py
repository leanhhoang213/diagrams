from diagrams import Cluster, Diagram, Edge
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
from diagrams.aws.security import IAM 
from diagrams.aws.management import Cloudtrail
from diagrams.aws.management import Config

graph_attr = {
    "splines": "ortho",
}

with Diagram("BASIC", show=False, graph_attr=graph_attr):
    with SystemBoundary("Audit & Governance", color="Black"):
        iam = IAM("IAM Roles")
        trail = Cloudtrail("Cloud Trail")
        config = Config("AWS Config")
    user = User("dev / user")
    with SystemBoundary("tool"):
        b = [
        Container(
            name="Dependency Check",
            technology="SCA"
        ),
        Custom("SonarQube", "sona.png")]
    with SystemBoundary("AWS codepipeline"):
        git = Git("Git")
        commit = Codecommit("AWS code commit")
        buil = Codebuild("AWS code build")
        deploy = Codedeploy("AWS code deploy")
        buil1 = Codebuild("AWS code build test")
        deploy1 = Codedeploy("AWS code deploy")
        a = [git >> Edge(color="Blue") >> commit >> Edge(color="Blue") >> buil >> Edge(color="Blue") >> deploy >> Edge(color="Blue") >> buil1 >> Edge(color="Blue") >> deploy1]
    elas = EB("AWS elastic (Staging)")
    elas1 = EB("AWS elastic (Production)")
    s3 = S3("AWS S3")
    lamd = Lambda("AWS Lambda")
    secuhub = SecurityHub("AWS securityhub")
    OW = Container(
        name="OWASP (DAST)"
    )
    
    MA = Container(
        name="Manual Approval"
    )
    user1 = User("domain/dev/user")
    mail = SimpleEmailServiceSesEmail("Email")
    sns = SNS("AWS SNS")
    cloudw = Cloudwatch("AWS cloudwatch events")
    cloudw1 = Cloudwatch("AWS cloudwatch logs")
    user >> Edge(color="Blue") >> git
    buil >> Edge(color="Blue") >> Edge(color="Blue") >> s3 << Edge(color="Blue") << lamd
    buil >> Edge(color="Blue") >> lamd >> Edge(color="Blue") >> secuhub
    buil1 >> Edge(color="Blue") >> OW
    deploy >> Edge(color="Blue") >> elas
    deploy1 >> Edge(color="Blue") >> elas1
    buil >> Edge(color="Blue") >> b
    a >> Edge(color="Black") >> sns
    a >> Edge(color="Black") >> cloudw
    a >> Edge(color="Black") >> cloudw1
    user1 << Edge(color="Black") << mail << Edge(color="Black") << sns << Edge(color="Black") << cloudw
    