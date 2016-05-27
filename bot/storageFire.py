from firebase import firebase

FIREBASE_URL = "https://staples-bot.firebaseio.com/"

class Storage(self, arg):
    def saveit(self, arg):
        fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application
        data = arg
        fb.put('/Testing/Node1', "Data", data) # Add data to Node Node1
    
    def loadit(self):
        fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application
        result = fb.get('/Testing', "Node1") # Get  data from firebase
        return result
