from getpass import getpass
from colorama import Fore
from instagram import Instagram

print(Fore.GREEN + """\n
                               /'                                                             /'                /'
                           --/'--                                                           /'              --/'--
     O  ,____     ____     /' ____     ____      ____     ____     ,__________            /'__     ____     /'    
   /'  /'    )  /'    )--/' /'    )  /'    )   )'    )--/'    )   /'    )     )         /'    )  /'    )--/'      
 /'  /'    /'  '---,   /' /'    /' /'    /'  /'       /'    /'  /'    /'    /'        /'    /' /'    /' /'        
(__/'    /(__(___,/   (__(___,/(__(___,/(__/'        (___,/(__/'    /'    /(__       (___,/(__(___,/'  (__        
                                     /'                                       -------                             
                             /     /'                                                                             
                            (___,/'                                                            twitter alii76tt                   
""")
    

print("Please Login!")
username = input("Your Username: ")
password =  getpass()
print("\nPlease Wait. Log in...")

instagram = Instagram(username=username, password=password)
instagram.signIn()
while True:
    try:
        choice = int(input("""
                Menu\n
                1- Get Followers\n
                2- Get Following\n
                3- Folow User\n
                4- UnFollow User\n
                5- Who Don't Follow Me\n
                6- Whatch Story\n
                7- Exit\n
                Choice: """))

        if choice == 1:
            instagram.getFollowers()
        elif choice == 2:
            instagram.getFollowing()
        elif choice == 3:
            howMany = int(input("How many people will you follow: "))

            if howMany == 1:
                user = input("Username: ")
                instagram.followUser(username=user)
            elif howMany > 1:
                for i in range(howMany):
                    user = input("Username: ")
                    instagram.followUser(username=user)
        elif choice == 4:
            howMany = int(input("How many people will you unfollow: "))

            if howMany == 1:
                user = input("Username: ")
                instagram.unFollowUser(username=user)
            elif howMany > 1:
                for i in range(howMany):
                    user = input("Username: ")
                    instagram.unFollowUser(username=user)
        elif choice == 5:
            instagram.whoDontFollowMe()
        elif choice == 6:
            user = input("Username: ")
            instagram.whatchStory(username = user)
        elif choice == 7:
            break
        else:
            "You entered incorrectly!"
    except KeyboardInterrupt:
        print("\n" + "Goodbye, Friend!")
        quit()