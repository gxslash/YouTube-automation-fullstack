import boto3
import json
import generator

BUCKET_NAME = 'subtopic'

def generate_s3_key(topic):
    return f'{topic}'

def upload_to_s3(file_content, bucket_name, s3_key):
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=s3_key, Body=file_content)

def lambda_handler(event, context):
    try:
        languages = event.get('languages')
        topic = event.get('topic')
        subtopics = generator.runner(topic=topic, langauges=languages)
        upload_to_s3(subtopics, BUCKET_NAME, s3_key=topic)
        # TODO: If the given topic already exists, update languages in RDS
        return {
            'statusCode': 200,
            'body': json.dumps('File successfully uploaded to S3')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
