def fileUpload(file):
    from firebase_admin import storage
    bucket = storage.bucket()
    blob = bucket.blob(file.name)
    blob.upload_from_filename(file.name)
    blob.make_public()
    print("your file url", blob.public_url)
    
