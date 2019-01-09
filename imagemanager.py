from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

client = storage.Client()
bucket = client.get_bucket("fihreebahsay.appspot.com")

imagepath = "pirate1.gif"
imageBlob = bucket.blob("images/" + imagepath)
imageBlob.upload_from_filename(imagepath)
