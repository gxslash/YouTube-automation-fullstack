import boto3
import json
import generator

BUCKET_NAME = 'content'

def generate_s3_key(lang, title):
    return f'{lang}/{title}'

def upload_to_s3(file_content, bucket_name, s3_key):
    s3 = boto3.client('s3')
    # save csv file or save into RDS
    # s3.put_object(Bucket=bucket_name, Key=s3_key, Body=file_content)

def lambda_handler(event, context):
    try:
        lang = event.get('lang')
        subtopic = event.get('subtopic')
        title, intro, transcript  = generator.runner(language=lang, subtopic=subtopic)
        s3_key = generate_s3_key(lang, title)
        upload_to_s3(transcript, BUCKET_NAME, s3_key)
        return {
            'statusCode': 200,
            'body': json.dumps('File successfully uploaded to S3')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
