class User:

    
    
    def registration_info(self, username, email):
        self.username = username
        self.email = email
        #return f"User {self.username} with email {self.email} has been registered."
        print(f"User {self.username} with email {self.email} has been registered.")
        
    

pk_obj = User()
pk_obj.registration_info('aryan', 'aryan@gmail.com')

print(pk_obj.__dict__)  # Output: {'username': 'aryan', 'email': 'aryan@gmail.com'} # dunder methhod or magic method 