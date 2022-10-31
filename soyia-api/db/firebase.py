from firebase_admin import credentials, initialize_app,get_app

def initializeApp():
    credential = credentials.Certificate('YOUR DOWNLOADED CREDENTIALS FILE (JSON)')
    options= {
        "databaseURL":"",
        'storageBucket': 'YOUR FIREBASE STORAGE PATH (without gs://)'
    }

    return initialize_app(credential, options)

def firebase_setup():
    try:
        return get_app()
    except:
        pass
    return initializeApp()
        
