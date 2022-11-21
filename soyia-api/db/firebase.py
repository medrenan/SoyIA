# import firebase_admin
# from firebase_admin import initialize_app,get_app,credentials
# from models.envVariables import privateKey,privateKeyId,projectId,clientEmail,clientId,clientCertUrl

# def initializeApp():
#     try:
#         cred = credentials.Certificate({
#         "type": "service_account",
#         "project_id": projectId,
#         "private_key_id": privateKeyId,
#         "private_key": privateKey,
#         "client_email": clientEmail,
#         "client_id": clientId,
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_x509_cert_url": clientCertUrl
#         })

#         options= {
#             "databaseURL":"https://soyia-api-default-rtdb.firebaseio.com",
#             'storageBucket': 'soyia-api.appspot.com'
#         }

#         app = firebase_admin.initialize_app(cred,options)
#         print("iniciado firebase com sucesso")
#         return app
#     except:
#         print("Houve um erro ao iniciar firebase")
#         pass

# def firebase_setup():
#     try:
#         app = get_app();
#         print("iniciado firebase com sucesso")
#         return app
#     except:
#         pass
#     return initializeApp()