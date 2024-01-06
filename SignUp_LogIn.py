
# Without GUI
import getpass
class signup():
    global u, p,l

    def sign_up(self):
        global u, p,l
        u = input('Enter Username: ').lower()
        while (True):
            # u = input('Enter Username: ').lower()
            p = getpass.getpass('Enter Password: ')
            p1 = getpass.getpass('Confirm Pass: ')
            if p1 != p:
                print(f"Passwords are different {p} {p1}")
                continue
            elif p == p1:
                print(f"Your User ID is : {u}")
                print(f"You Password is : {p1}")
                print('----------------------------------------------')
                print()
                print('----------------------------------------------')
                l = input("Press 'L' to Login: ")
                break


obj1 = signup()


class login(signup):
    global u, p,l

    def log_in(self):
        global u, p,l
        if l=='L' or l=='l':
         while (True):
            i = input('Enter the username: ')
            if i != u:
                print('Incorrect Username')
                continue
            elif i == u:
                break


obj2 = login()


class Password(login):
    global u,p,l

    def My_password(self):
              global u,p,l
              while(True):
                   p2 = input('Enter Password: ')
                   if p2==p:
                        print('LogIn Successful')
                        break
                   else:
                        print('Incorrect Password')
                        continue

obj3 = Password()



obj1.sign_up()
obj2.log_in()
obj3.My_password()

