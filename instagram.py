from traceback import print_tb
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
import time
  
class Instagram():
    def __init__(self, username, password):
        self.browserProfile = FirefoxProfile()
        self.browserProfile.set_preference("intl.accept_languages", "en-US") # browser languages
        self.browser = webdriver.Firefox(firefox_profile=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)

        emailInput = self.browser.find_element_by_name("username")
        passwordInput = self.browser.find_element_by_name("password")
        emailInput.send_keys("" + self.username)
        passwordInput.send_keys("" + self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

        try:
            if self.browser.find_element_by_css_selector(".eiCW-"):
                print("Your password incorrect!")
                quit()
        except:
            print("Login successful.")
            
        time.sleep(5)

        

    def getFollowers(self):
        self.browser.get(
            f"https://www.instagram.com/{self.username}")
        time.sleep(3)

        try:

            self.browser.find_element_by_xpath(
                "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a").click()

            Instagram.scrollDown(self)
            
            followers = self.browser.find_elements_by_css_selector(
                    ".FPmhX.notranslate._0imsa")
            
            list = []
            number = 0
            for follower in followers:
                number += 1
                print(f"{number}" + " --> " + follower.text)
                list.append(follower.text)
            
            with open("followers.txt", "w", encoding="utf8") as file:
                for follower in list:
                    file.write(f"{follower}\n")
        except Exception:
            print("No one is following you.")

    def getFollowing(self):
        self.browser.get(
            f"https://www.instagram.com/{self.username}")
        time.sleep(3)

        try:

            self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]").click()   

            Instagram.scrollDown(self)
            following = self.browser.find_elements_by_css_selector(
                        ".FPmhX.notranslate._0imsa")
                
            list = []
            number = 0
            for follow in following:
                number += 1
                print(f"{number}" + " --> " + follow.text)
                list.append(follow.text)
            
            with open("following.txt", "w", encoding="utf8") as file:
                    for follower in list:
                        file.write(f"{follower}\n")
        except Exception:
            print("You aren't following anyone.")
    
    def followUser(self, username): 
        self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(4)
                 
        
        try:
            try:
                self.browser.find_element_by_css_selector("._5f5mN.jIbKX._6VtSN.yZn4P").click()
            except:     
                self.browser.find_element_by_css_selector(".sqdOP.L3NKy.y3zKF").click()
            print(f"{username} is following.")
            
        except Exception:
            button = self.browser.find_element_by_css_selector("._5f5mN.-fzfL._6VtSN.yZn4P")
            print(f"Already follow {username}.")

    def unFollowUser(self,username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(4)
         
        try:
            self.browser.find_element_by_css_selector("._5f5mN.jIbKX._6VtSN.yZn4P")
            print(f"You don't already follow {username}.")
        except:
            try:
                self.browser.find_element_by_css_selector("._5f5mN.-fzfL._6VtSN.yZn4P").click()
            except:
                self.browser.find_element_by_css_selector(".qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.soMvl").click()
                   
            unFollow = self.browser.find_element_by_css_selector(".aOOlW.-Cab_")
            time.sleep(3)
            unFollow.click()
            print(f"{username} unfollowed.")

    def whoDontFollowMe(self):
        self.followers = []
        self.following = []
        self.dontfollow = []
        
        with open("followers.txt", "r") as file:
            for i in file:
                self.followers.append(i.strip())
        with open("following.txt", "r") as file2:
            for i in file2:
                self.following.append(i.strip())

        print("Users who do not follow you:".center(25,"*"))
        print()
        for user in self.following:
            if not user in self.followers:
                self.dontfollow.append(user)
                print(user)
                
        result = input("Would you like to unfollow people who don't follow you(all)?(Y/N): ")
        if result == "Y":
            for user in self.dontfollow:
                Instagram.unFollowUser(self,user)
        else:
            print("I haven't unfollowed anyone.")
    
    def whatchStory(self, username):
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(2)   

        try:
            self.browser.find_element_by_css_selector("._6q-tv").click()
        except Exception:
            print("Something went wrong.")
    
    def scrollDown(self):
        # Javascript commands

        jsCommand = """
        page = document.querySelector(".isgrP");
        page.scrollTo(0,page.scrollHeight);
        var pageDown = page.scrollHeight;
        return pageDown;
        """
        pageDown = self.browser.execute_script(jsCommand)

        while True:
            end = pageDown
            time.sleep(1)
            pageDown = self.browser.execute_script(jsCommand)
            if end == pageDown:
                break    