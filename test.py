import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyB7P2TBuIvdKqDx8ovsOy9phB4KvUpULH0",
    'authDomain': "efficiency-calculator.firebaseapp.com",
    'projectId': "efficiency-calculator",
    'storageBucket': "efficiency-calculator.appspot.com",
    'messagingSenderId': "1037551695369",
    'appId': "1:1037551695369:web:d27c3d72cbf583aaadaad8",
    'measurementId': "G-9QYEF7L9Q1"
}

firebase = pyrebase.initialize_app(firebaseConfig)

# setting up storage
storage = firebase.storage()

# upload files to storage
file = input("Enter the filename: ")
cloudfilename = input("Enter the cloud filename: ")
storage.child(cloudfilename).put(file)