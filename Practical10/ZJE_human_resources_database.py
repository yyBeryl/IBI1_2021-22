class Staff():#create a class include the needed information of staffs
    def __init__(self,first_name,last_name,location,role):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.role=role
    def info(self):
#report the required information
        print(self.first_name+" "+self.last_name+" is a "+self.role+" in "+self.location+".")
#an example
staff=Staff('Emma','White','International Campus or Edinburgh','counselor')
Staff.info(staff)
