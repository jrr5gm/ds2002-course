#!/bin/bash

import logging
import boto3
from botocore.exceptions import ClientError
s3 = boto3.client('s3', region_name='us-east-1')

def download_file(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
    except Exception:
        pass

url = "https://dogtime.com/wp-content/uploads/sites/12/2023/11/GettyImages-537870596-e1701102761329.jpg?w=1024"
save_path = 'dog.jpg'
download_file(url, save_path)

bucket = 'ds2002-jrr5gm'
local_file = 'dog.jpg'
resp = s3.put_object(Body = local_file, Bucket = bucket, Key = local_file, ACL = 'public-read')


def create_presigned_url(bucket_name, object_name, expiration=604800):

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket,
                                                            'Key': local_file},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

create_presigned_url(bucket, local_file, expiration=604800)


