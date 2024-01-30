### firebase
import pyrebase

config = {
    "apiKey": "AIzaSyB7P2TBuIvdKqDx8ovsOy9phB4KvUpULH0",
    "authDomain": "efficiency-calculator.firebaseapp.com",
    "projectId": "efficiency-calculator",
    "storageBucket": "efficiency-calculator.appspot.com",
    "messagingSenderId": "1037551695369",
    "appId": "1:1037551695369:web:d27c3d72cbf583aaadaad8",
    "measurementId": "G-9QYEF7L9Q1"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

email = input("Enter your email: ")
password = input("Enter your password: ")

user = auth.create_user_with_email_and_password(email, password)

auth.get_account_info(user['idToken'])

### firebase