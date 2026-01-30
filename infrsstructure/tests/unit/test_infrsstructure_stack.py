import aws_cdk as core
import aws_cdk.assertions as assertions

from infrsstructure.infrsstructure_stack import InfrsstructureStack

# example tests. To run these tests, uncomment this file along with the example
# resource in infrsstructure/infrsstructure_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = InfrsstructureStack(app, "infrsstructure")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
