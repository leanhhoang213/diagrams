from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

with Diagram("Event Processing", show=False):
	h1 = EKS("k8s")
	h2 = S3("event s3")
	h3 = Redshift("event r")

	with Cluster("Even fl"):
		with Cluster("Event wk"):
			h4 = [ECS("w1"),
				ECS("w2"),
				ECS("w3")]
		h5 = SQS("event SQS")
		with Cluster("Processing"):
			h6 = [Lambda("p1"),
				Lambda("p2"),
				Lambda("p3")]
	h1 >> h4
	h4 >> h5 >> h6
	h6 >> h2
	h6 >> h3
