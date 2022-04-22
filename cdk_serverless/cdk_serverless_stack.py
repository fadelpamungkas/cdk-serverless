from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from . import serverless


class CdkServerlessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        serverless.WidgetService(self, "Widgets")
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkServerlessQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
