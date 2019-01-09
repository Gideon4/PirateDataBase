from google.cloud import storage
import os
import datetime

class ImageManager:

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

    client = storage.Client()
    bucket = client.get_bucket("fihreebahsay.appspot.com")
    url = ""
    imagepath = "pirate1.gif"

    def uploadImage(self):
        imageBlob = self.bucket.blob("images/" + imagepath)
        imageBlob.upload_from_filename(imagepath)
        d = datetime.datetime(3005,12,5)
        self.url = imageBlob.generate_signed_url(d)

