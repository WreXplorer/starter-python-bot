from firebase import firebase

FIREBASE_URL = "https://staples-bot.firebaseio.com/"

class Storage:
    def saveit(self, arg):
        fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application
        data = arg
        fb.put('/Testing/Node1', "Data", data) # Add data to Node Node1
    def loadit(self):
        fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application
        result = str(fb.get('/Testing', "")) # Get  data from firebase
        result = result.split('u')
        return result
