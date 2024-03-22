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

https://ds2002-jrr5gm.s3.amazonaws.com/dog.jpg?AWSAccessKeyId=ASIA3FLDXPZXOWP2WXYP&Signature=gHzY94tg5smkjuTxMNdS5vOQdI0%3D&x-amz-security-token=FwoGZXIvYXdzEEUaDH2DXgac%2BLKoTMSAUiLEASQqsIe%2FiFaXvzun5%2FdZRZb8EK8LERfzetNOfg5yc47ybVOvUE7WC%2BadAIXvxUQawod9e%2F1iQ0rCi%2By1ORbGAivXeFR6UBxPUQGqHZzo8q7gIJ0eA95pDcXalUpLOtca9MkItO4QpxAtOBuiDVeMiAzIxEc0U8F1zyri5WUEgqappAFDCmZbYu8Sc56CmuEn027r9XoB7TeBVfyUjke0jIgyov7BqSuzw39DarBp1%2BUNgEdgFP87gr%2B92TgX8b98kH5bLcEo0rX3rwYyLcSA5S7Kyj2ORkhfmNxz08KhnZ5szNvgVDKLKblqp4EV02oHqsTIqlNS1cQsXQ%3D%3D&Expires=1711749638'