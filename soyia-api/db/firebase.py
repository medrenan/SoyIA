import firebase_admin
from firebase_admin import initialize_app,get_app,credentials

def initializeApp():
    try:
        cred = credentials.Certificate("./service_account.json")
        options= {
            "databaseURL":"https://soyia-api-default-rtdb.firebaseio.com",
            'storageBucket': 'soyia-api.appspot.com'
        }

        app = firebase_admin.initialize_app(cred)
        print("iniciado firebase com sucesso")
        return app
    except:
        print("Houve um erro ao iniciar firebase")
        pass

def firebase_setup():
    try:
        app = get_app();
        print("iniciado firebase com sucesso")
        return app
    except:
        pass
    return initializeApp()

# const firebaseConfig : any = {
#     apiKey: "AIzaSyA539sEfikhamS_I6WCBbVTYNMo3Btbtgs",
#     appId: "1:625773996693:android:170e3ff34b7f5e58b4c99c",
#     projectId: "soyia-api",
#     databaseURL: "https://soyia-api-default-rtdb.firebaseio.com",
#     messagingSenderId: '625773996693',
#     storageBucket: "soyia-api.appspot.com",
# };