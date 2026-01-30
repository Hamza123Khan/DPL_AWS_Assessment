# DPL_AWS_Assessment
# This repository contains DPL Assessment for AWS cloud engineer


Before running the CDK or deploying Lambda functions, ensure you have:
```
AWS Account with sufficient permissions (IAM role for CDK deployment)
AWS CLI installed and configured
Node.js >= 20 (for CDK CLI)
Python >= 3.12
CDK CLI installed globally:
```
Run this globallay to install AWS CDK
```
npm install -g aws-cdk
```
Run below command to configure the aws cli 
```
npm install -g aws-cdk
```
Install dependencies for cdk and create venv if required
```
python -m venv env
pip install -r requirement.txt
pip install aws-cdk-lib.aws-lambda-python-alpha
```
Bootstrap Infrastructure
```
npm cdk bootstrap
npm cdk deploy
or
npx cdk bootstrap
npx cdk deploy
```
To check the response of the application via apigatway use curl
```
curl -X POST "https://YOUR_API_ID.execute-api.YOUR_REGION.amazonaws.com/prod/prompt" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Write a 1-line motivational quote"}'
```
# run Runs on push to main branch
```
Installs dependencies (Python & Node)
Deploys CDK stacks
Sends Slack notifications on success or failure
```
# Secret Name	Description
```
AWS_ROLE_ARN	IAM role for CDK deployment
AWS_REGION	AWS region to deploy (e.g., us-east-1)
SLACK_WEBHOOK_URL	Slack webhook for deployment notifications
```

# The architecture consist of 
* api gateway from where the request will be send to lambda
* lamabda function which will extract the prompt and make an actual request to bedrock model which is "amazon.titan-text-lite-v1"
* After that the resposne from model will be send to user
* used the least expensive model where there is no requirement for like Anthropic model where you need to first give request to Anthropic to use their model
* total estemated cost will be 10 to 15$ involving all infra like s3, bedrock model, lambda and apigateway
