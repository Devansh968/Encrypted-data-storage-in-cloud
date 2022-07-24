import encryption
import menuTypes
import users
import googleDriveAPI
import eel
eel.init("FrontEnd_EEL")
eel.start("index.html")



def main():
    # Checking if key exists
    e = encryption
    # key = e.keyRead()
    try:
        while True:
            u = users
            m = menuTypes
            # Checking if any users exists, if they don't then a new user will have to be created
            if(u.accounts == 0):
                print(
                    "\nYou must create an admin account. Please set username as 'admin'\n")
                u.newUser()
            else:
                #Log in screen
                u.login()

                # Admin has their own menu and standard user has their own specific menu
                if u.privilege:
                    m.privilegeMenu()
                else:
                    m.standardMenu()

    except Exception:
        pass


if __name__ == "__main__":
    main()