from google.cloud import storage

import os

current_directory = os.path.dirname(os.path.abspath(__file__))

keys_path = os.path.join(current_directory, '../../keys.json')
client = storage.Client.from_service_account_json(keys_path)


def upload_file(file, destination, bucket):
    bucket = client.get_bucket(bucket)
    blob = bucket.blob(destination)
    blob.upload_from_file(file)
    return blob.public_url
