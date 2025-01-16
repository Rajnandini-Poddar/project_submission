import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'your-s3-bucket-name'
    file_content = event['file_content']
    file_name = event['file_name']

    s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
    return {"statusCode": 200, "message": f"File {file_name} stored successfully in {bucket_name}."}
