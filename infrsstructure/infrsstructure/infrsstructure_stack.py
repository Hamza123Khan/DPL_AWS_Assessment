from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    aws_iam as iam,
)
import aws_cdk as cdk
from constructs import Construct
from aws_cdk.aws_lambda_python_alpha import PythonFunction
class InfrsstructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bedrock_lambda = lambda_.Function(
            self, 'BedrockApiHandler',
            runtime= lambda_.Runtime.PYTHON_3_12,
            code=lambda_.Code.from_asset("../Lambda_function"),
            handler="App.handler",
            timeout= cdk.Duration.seconds(50),
            memory_size=256,
        )
        bedrock_lambda.add_to_role_policy(iam.PolicyStatement(
            actions=["bedrock:InvokeModel",
            "bedrock:InvokeModelWithResponseStream"],
            
            resources= ["*"], 
        ))
        api = apigateway.LambdaRestApi(
            self, "bBedrockApiEndpoint",
            handler = bedrock_lambda,
            proxy=True,
        )
        cdk.CfnOutput(self, "ApiUrl", value=api.url)