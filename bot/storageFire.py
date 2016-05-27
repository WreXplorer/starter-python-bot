from firebase import firebase

FIREBASE_URL = "https://staples-bot.firebaseio.com/"

class Storage:
    def saveit(self, data, value):
        fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application
        fb.put('/Lists/Todo', data, value) # Add data to Node Node1
    def loadit(self):
        fb = firebase.FirebaseApplication(FIREBASE_URL, None) # Create a reference to the Firebase Application
        results = []
        for x in fb.get('/Lists/Todo', None):
            results[x] = fb.get('/Lists/Todo', str(x))
        
        return results[1]
