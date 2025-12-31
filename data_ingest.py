# Example GCS upload
from google.cloud import storage
def upload_file(bucket_name, source_file, dest_blob):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(dest_blob)
    blob.upload_from_filename(source_file)
    print('uploaded', source_file)
