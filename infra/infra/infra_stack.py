import os

from aws_cdk import (
    CfnOutput,
    Duration,
    RemovalPolicy,
    Stack,
    aws_apigatewayv2 as apigwv2,
    aws_apigatewayv2_integrations as apigwv2_integrations,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_logs as logs,
)
from constructs import Construct
from constructs import Construct

class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create telemetry_history_table
        telemetry_history_table = dynamodb.Table(
            self,
            "telemetry_history_table",
            table_name="telemetry_history_table",
            partition_key=dynamodb.Attribute(
                name="edge_id",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="timestamp",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY
        )

        # create lambda function
        telemetry_function_get = lambda_.Function(
            self,
            "telemetry_function_get",
            function_name="telemetry_function_get",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="get.get.handler",
            code=lambda_.Code.from_asset(os.path.join(os.path.dirname(__file__), "../../lambda_src/telemetry")),
            timeout=Duration.seconds(30),
            memory_size=128,
            environment={
                "TABLE_NAME": telemetry_history_table.table_name,
            },
            log_retention=logs.RetentionDays.ONE_WEEK,
        )

        telemetry_function_post = lambda_.Function(
            self,
            "telemetry_function_post",
            function_name="telemetry_function_post",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="post.post.handler",
            code=lambda_.Code.from_asset(os.path.join(os.path.dirname(__file__), "../../lambda_src/telemetry")),
            timeout=Duration.seconds(30),
            memory_size=128,
            environment={
                "TABLE_NAME": telemetry_history_table.table_name,
            },
            log_retention=logs.RetentionDays.ONE_WEEK,
        )


        # grant lambda function permissions to access the DynamoDB table
        telemetry_history_table.grant_read_data(telemetry_function_get)
        telemetry_history_table.grant_write_data(telemetry_function_post)

        # create API Gateway HTTP API
        http_api = apigwv2.HttpApi(
            self,
            "telemetry_api",
            api_name="telemetry_api",
            create_default_stage=True,
        )

        # create API Gateway integration for the lambda function
        lambda_integration_get = apigwv2_integrations.HttpLambdaIntegration(
            "lambda_integration_get",
            handler=telemetry_function_get,
        )

        lambda_integration_post = apigwv2_integrations.HttpLambdaIntegration(
            "lambda_integration_post",
            handler=telemetry_function_post,
        )

        # add a route to the API Gateway for the lambda function
        http_api.add_routes(
            path="/telemetry",
            methods=[apigwv2.HttpMethod.GET],
            integration=lambda_integration_get,
        )
        
        http_api.add_routes(
            path="/telemetry",
            methods=[apigwv2.HttpMethod.POST],
            integration=lambda_integration_post,
        )

        # output the API Gateway URL
        CfnOutput(
            self,
            "ApiUrl",
            value=http_api.url,
            description="The URL of the API Gateway",
        )

        

