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
        blob.upload_from_file(file)
        blob.make_public()
        res = make_response({"mensagem":"imagem baixada em: "+blob.public_url},200)
        return res
    except:
        res = make_response({"mensagem":"Houve um erro ao tentar fazer upload da mensagem"},400)
        return res

