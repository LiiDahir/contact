from contact import Contact
import time
obj_con = Contact()
class User:
    def __init__(self):
        obj_con.load_data('user')
    def show_status(self):
        print("1. Login")
        print("2. Signup")
        select = obj_con.is_int("select one of them : ",2)
        if select ==1:
            self.login()
        elif select ==2:
            self.add()
    def add(self):
        full_name = obj_con.promt("Enter The Name : ",'str',obj_con.check_name)
        phone = obj_con.promt("Enter The phone : ",'int',obj_con.check_number)
        gmail = obj_con.promt("Enter The gmail : ",'str',obj_con.check_gmail)
        username = input("Enter The username : ")
        pin = input("Enter The password : ")
        con_pin = input("Enter The confirm password : ")
        while pin != con_pin:
            print("pin is not matching....")
            pin = input("Enter The password : ")
            con_pin = input("Enter The confirm password : ")
        id = len(obj_con.user)
        obj_con.user[id]=[full_name,phone,gmail,username,pin]
        obj_con.write_data()
        self.show_status()
    def login(self):
        username = self.Search("Enter The username : ")
        while username == False:
                username = self.Search("Enter The correct username : ")
        password = input("Enter the pin : ")
        count,time_span = 2 ,5
        while username[0][4] != password:
            count-=1
            password = input("Enter the correct pin you "+str(count+1)+" : ")
            if count <=0:
                time.sleep(time_span)
                time_span*=2
                count = 3

    def Search(self,promt):
        target = input(promt).lower()
        matches = [ {id:data} for id,data in obj_con.user.items() if target == data[3]]
        if len(matches) == 0:
            return False
        else:
            return matches[0]
obj = User()
obj.show_status()