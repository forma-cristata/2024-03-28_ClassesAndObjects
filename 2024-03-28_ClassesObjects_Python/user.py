class User:
    def __init__(self, first_name, last_name, birth_date, relationship_status):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.relationship_status = relationship_status
        self.login_attempts = 0
    def describe_user(self):
        """Prints the user's attributes in a single sentence"""
        print(f"{str(self.first_name).title()} {str(self.last_name).title()} was born on {self.birth_date} and is {self.relationship_status}\n")
    def greet_user(self):
        """Prints a greeting to the user in question (self)"""
        print(f"Hello {str(self.first_name).title()} {str(self.last_name).title()}! How are you today?\n\n")
    def increment_login_attempts(self):
        """Increments the login attempts of a user"""
        self.login_attempts += 1
    def reset_login_attempts(self):
        """Resets the login attempts of the user to zero"""
        self.login_attempts = 0
        
if __name__ == "__main__":
    users = [User("Kaci", "Craycraft", "04/19/1996", "in a relationship"), 
            User("Rachel", "Henninger", "03/12/1996", "in a relationship"),
            User("Kevin", "Todd", "01/06/1923", "single"),
            User("Logan", "Brooks", "01/02/2003", "single")]
    for user in users:
        user.describe_user()
        user.greet_user()
        
    #4
    for i in range(0,5):
        users[0].increment_login_attempts()
        print(f"{users[0].first_name} has attempted login {users[0].login_attempts} times.")
    users[0].reset_login_attempts()
    print(f"\n{users[0].first_name}'s login attempts: {users[0].login_attempts}")

