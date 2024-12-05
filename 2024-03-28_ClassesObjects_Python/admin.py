from user import User

class Privileges:
    def __init__(self, privileges: list = ['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges
    def show_privileges(self):
        print(f"Admin's privileges: ", end='')
        for privilege in self.privileges:
            print(privilege.title(), end=", ")
            
class Admin(User):
    def __init__(self, first_name, last_name, birth_date, relationship_status):
        super().__init__(first_name, last_name, birth_date, relationship_status)
        self.privileges = Privileges()

if __name__ == "__main__":           
    #new_user = Admin("Kaci", "Craycraft", "04/19/1996", "in a relationship", ['can add post', 'can delete post', 'can ban user'])
    #new_user.show_privileges()
    
    admin_q7 = Admin("Stephen", "Weaver", "12/01/1989", "in a relationship")
    admin_q7.privileges.show_privileges()