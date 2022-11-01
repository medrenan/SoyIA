from datetime import date

from flask import make_response

def filePath(file,folderPath):
    extension = file.filename.split('.').pop();
    fileName = f'{date.today()}.{extension}'
    return f'{folderPath}/{fileName}'

def fileUpload(file,folderPath):
    try:
        fileName = filePath(file,folderPath)

        from firebase_admin import storage
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)
        blob.make_public()
        print("your file url", blob.public_url)
    except Exception as inst:
        print(inst.args)
        res = make_response({"mensagem":"Houve um erro ao tentar fazer upload da mensagem"},400)
        return res

