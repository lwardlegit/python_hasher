import random
import string
import bcrypt


class Hash_maker:
    def __init__(self, name):
        self.name = name
        self.length = 16
        self.value = ''
        self.hash = ''
   
    def random_string(self):
        count = 0
        password = ''
        while count < 15:
            password+=random.choice(string.ascii_letters)
            count+=1
        self.value = password.encode()
        

    def hash_string(self):
        salt = bcrypt.gensalt()
        self.hash = bcrypt.hashpw(self.value, salt)
        
    
