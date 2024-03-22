
aws s3 cp puppy.jpg s3://ds2002-jrr5gm/
aws s3 presign --expires-in 604800 s3://ds2002-jrr5gm/puppy.jpg

#URL
https://ds2002-jrr5gm.s3.us-east-1.amazonaws.com/puppy.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA3FLDXPZXGF3DCM3C%2F20240319%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240319T210229Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDAw5u8fP3QmJpcTOQSLEAYktw0xEkgzhaR2g3gyoArlHrkHMd7n434z%2FOdKnn9HfjCDRFT8a91gPTsM7ZGHG45ikyqBjC4JKV94%2BcdkuaFiG%2BH0I5zlQfwtYmTgVyChs2tCo2dhe5mV2uxdTBUDwekfX8b%2BZPwBVaN6nyPLcFNrhtQAol4BXDc%2BOvBAzg0g2DKKAijIjfMUB5C0a87V9OTL%2BRP586M1A6pumRrvhO9INCdtN4q5KoDe4I9KKkIaroVEyNdXfRW2qHN3bQ7wmrwXFTv8osfDnrwYyLZaonMPMcFyxYa3SzwUkl3zvAD5W5HLsw4SmiTURYShxx8wrpiDXkowzpjdWiw%3D%3D&X-Amz-Signature=a907d61235eaa5e2b6cf7be4315d14fba2bc89f60918afedac1439713cfe95f5

