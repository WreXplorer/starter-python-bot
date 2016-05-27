from firebase import firebase

FIREBASE_URL = "https://staples-bot.firebaseio.com/"

class Storage:
    def saveit(self, data, value):
        fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application
        fb.put('/Lists', data, value) # Add data to Node Node1
    def loadit(self):
        fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application
        results = fb.get('/Lists/Todo', "1") # Get  data from firebase
        
        return results
