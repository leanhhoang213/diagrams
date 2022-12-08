from diagrams import Cluster, Diagram
from diagrams.c4 import SystemBoundary
from diagrams.aws.management import Cloudwatch
from diagrams.aws.compute import Lambda
from diagrams.aws.database import DDB
from diagrams.aws.integration import SNS
from diagrams.aws.network import VPC
from diagrams.aws.compute import EC2
from diagrams.aws.management import AutoScaling
from diagrams.aws.storage import EFS
from diagrams.aws.storage import S3

graph_attr = {
    "splines": "ortho",
}

with Diagram("DEMO", show=False, graph_attr=graph_attr):
	h1 = Cloudwatch("Amazon CloudWatch")
	h2 = Lambda("AWS Lambda")
	h9 = S3("AWS S3")
	h1 >> h2
	h3 = DDB("AWS DynamoDB")

	
	with Cluster("VPC"):
		with SystemBoundary("1"):
			h5 = AutoScaling("aws Auto Scaling group")
			h6 = EC2("AWS EC2")
			[h5,
			h6]

		h6 >> [EFS("AWS EFS (source)"),
			EFS("AWS EFS (backup)")]
	h4 = SNS("AWS SNS")
	h2 >> h4
	h2 >> h6 >> h9
	h2 >> h3 << h6
	

	


