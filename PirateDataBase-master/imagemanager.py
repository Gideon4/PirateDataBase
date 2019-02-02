from google.cloud import storage
from PIL import Image, ImageTk
import os, io, urllib
import datetime

class ImageManager:

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

    client = storage.Client()
    bucket = client.get_bucket("fihreebahsay.appspot.com")
    url = ""
    imagepath = "pirate7.gif"

    def uploadImage(self):
        imageBlob = self.bucket.blob("images/" + os.path.basename(self.imagepath))
        imageBlob.upload_from_filename(self.imagepath)
        d = datetime.datetime(3005,12,5)
        self.url = imageBlob.generate_signed_url(d)

    def downloadurl(self):
        rawdata = urllib.request.urlopen(self.url).read()
        img = Image.open(io.BytesIO(rawdata))
        imgtk = ImageTk.PhotoImage(img)
        return(imgtk)

