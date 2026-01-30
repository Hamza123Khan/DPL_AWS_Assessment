import boto3
import json

bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

MODEL_ID = "amazon.titan-text-lite-v1"

def handler(event, context):
    try:
        body_json = json.loads(event.get("body", "{}"))
        prompt = body_json.get("prompt", "Hello")

        request_body = json.dumps({
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 2048,
                "temperature": 0.7,
                "topP": 0.9
            }
        })

        response = bedrock_runtime.invoke_model(
            modelId=MODEL_ID,
            body=request_body,
            contentType="application/json",
            accept="application/json"
        )

        raw_body = response["body"]

        # handle StreamingBody OR str OR bytes
        if hasattr(raw_body, "read"):
            raw_body = raw_body.read()

        if isinstance(raw_body, (bytes, bytearray)):
            raw_body = raw_body.decode("utf-8")

        response_body = json.loads(raw_body)

        generated_text = response_body["results"][0]["outputText"]

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"response": generated_text})
        }

    except Exception as e:
        print(f"Error invoking Bedrock model: {e}")
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
