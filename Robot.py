from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os


class INSTABOT:

    def __init__(self):
        self.PATH = os.path.join(os.path.expanduser("~"), "chromedriver.exe")
        self.browser = webdriver.Chrome(self.PATH)
        self.URL = "https://www.instagram.com"
        self.Dump_Account_Exceptions_FilePath = None
        self.Access_Account_Credentials_FilePath = None
        return
    
    def __del__(self):
        self.close()
        return
    
    def login(self, username, password):
        #Find the text to type in the username
        trials = 2
        tries = 1

        while(tries <= trials):
            try:
                time.sleep(0.4)
                UsernameButton = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Phone number, username, or email']")
                UsernameButton.send_keys(username)
                break

            except Exception as e:
                time.sleep(0.8)
                #UsernameButton = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Phone number, username, or email']")
                #UsernameButton.send_keys(username)
            
            tries = tries + 1
        
        if(tries >= trials): return False
        
        #Find the password textbox type in the password
        time.sleep(0.2)
        PassButton = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Password'")
        PassButton.send_keys(password)
        
        #CLICK THE LOGIN BUTTON
        time.sleep(0.2)
        try:
            LOGIN = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button")
            LOGIN.click()
            return True
        except Exception as e:
            return False
         
    def logout(self):
        #IDENTIFIER FOR THE ELEMENT
        property = ".x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xh8yej3.x193iq5w.x1lliihq.x1dm5mii.x16mil14.xiojian.x1yutycm"
        
        time.sleep(0.4)
        #Find the MORE button for options and click it
        MORE = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Settings']")
        MORE.click()
        
        time.sleep(0.3)
        #Find the Logout button in MORE now, and click it
        LOGOUT = self.browser.find_elements(By.CSS_SELECTOR, property)
        pos = len(LOGOUT)-1
        LOGOUT[pos].click()
        time.sleep(0.4)
        return True
 
    def settings(self):

        #IDENTIFIER FOR THE ELEMENT TO FIND
        property = ".x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xh8yej3.x193iq5w.x1lliihq.x1dm5mii.x16mil14.xiojian.x1yutycm"
        TrialLimit = 2
        Tries = 1

        #Find the MORE option button and click it
        while(Tries <= TrialLimit):
        #Try to click the option, sometimes option doesn't load in html page or could be that there was some error in login page like pass incorrect etc
            try:
                time.sleep(0.7)
                MORE = self.browser.find_element(By.CSS_SELECTOR, ".xl5mz7h.xhuyl8g").click()
                break

            except Exception as e:
                time.sleep(1)
            Tries = Tries + 1
        

        if(Tries >= TrialLimit):return False
        time.sleep(1)
        #NOW Click on the 'Settings' option
        OPTION = self.browser.find_elements(By.CSS_SELECTOR, property)
        #STORED all the elements from 'Settings' to 'Logout' because it was hard to uniquely identify. Using their position we can click them
        pos = len(OPTION)-1
        OPTION[0].click()
        return True
    
    def resetpassword(self, name, Pass, NEW_PASS):
        
        if(Pass == NEW_PASS):
            return False
        #Identifier for the ELEMENTs
        trials = 2
        tries = 1
        property = ".x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1xmf6yo.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1"
        
        #CLICK on the ACCOUNT CENTER, specifically click on 'Password and Security'
        while(tries <= trials):
            try:
                time.sleep(0.3)
                OPTIONS = self.browser.find_elements(By.CSS_SELECTOR, property)
                OPTIONS[0].click()
                break
            except Exception:
                time.sleep(2)
                pass

            tries = tries + 1
        if(tries >= trials): return False

        #Click on 'Password and Security' again here as this is the real option
        time.sleep(0.4)
        PASS_SECURITY = self.browser.find_element(By.LINK_TEXT, "Password and security")
        PASS_SECURITY.click()
        time.sleep(0.6)
        
        #Click on Change pass here
        CHANGE_PASS = self.browser.find_element(By.CSS_SELECTOR, "[aria-label='Change password'").click()
        
        #Click on the profile that will show up to choose from. Make sure to select the profile that matches username
        #UPDATE: This technique only works if a single account profile shows up, if more than one shows up. It won't work
        user = "//span[text()='" + name + "']"
        time.sleep(0.5)
        try:
            ACCOUNT = self.browser.find_element(By.XPATH, user).click()
        except Exception:
            return False
        
        #Locate the Current password button and type in it the current pass
        time.sleep(1)
        tries = 1
        while(tries <= trials):
            try:
                CurrPass = self.browser.find_element(By.XPATH, "(//input[@type='password'])[last()-2]")
                CurrPass.send_keys(Pass)
                break

            except Exception as e:
                time.sleep(1.5)
                #CurrPass = self.browser.find_element(By.XPATH, "(//input[@type='password'])[last()-2]")
                #CurrPass.send_keys(Pass)
            tries = tries + 1
        
        if(tries >= trials): return False

        #Locate the new password button and type in the new password
        time.sleep(0.01)
        NewPass = self.browser.find_element(By.XPATH, "(//input[@type='password'])[last()-1]")
        NewPass.send_keys(NEW_PASS)
        
        
        # Locate the retype button to retype the new password
        time.sleep(0.02)
        RetypePass = self.browser.find_element(By.XPATH, "(//input[@type='password'])[last()]")
        RetypePass.send_keys(NEW_PASS)
        
         
        #click on confirm change button
        time.sleep(0.1)
        ChangeButton = self.browser.find_element(By.XPATH,  "(//span[text()='Change password'])[last()]").click()
        time.sleep(3)
        

        #Note Need to check if the account password for reset actually got reset, because incase the passwords don't match criterion, program will still return true incase
        try:
            self.browser.back()
            time.sleep(0.4)
            self.browser.back()
            time.sleep(0.4)
            self.browser.back()
            time.sleep(0.4)
            self.browser.back()
        except Exception:
            #Here we're returning true because, since we already clicked change button, now after that if any exception occurs the password would have been changed anyway
            return True
        
        #Checks if the notification box will appear or not
        time.sleep(0.4)
        try:
            NOTNOW = self.browser.find_element(By.XPATH, '//button[contains(text(), "Not Now")]')
            NOTNOW.click()
        
        except NoSuchElementException:
            pass
        
        return True
            
    def run(self, username, password, newpass, RUN = "single"):
        #Run this only when single is selected, to use this function seperately
        if(RUN == "single"): self.browser.get(self.URL)
        
        time.sleep(2)
        if(self.login(username, password) == False): return False
        time.sleep(2.3)
        if(self.settings() == False): return False
        time.sleep(1.3)
        if(self.resetpassword(username, password, newpass) == False): return False
        time.sleep(0.5)
        if(self.logout() == False): return False
        time.sleep(0.3)
        return True
    
    def SpecifyFilePath(self, access, dump):
        self.Access_Account_Credentials_FilePath = access
        self.Dump_Account_Exceptions_FilePath = dump


    def runfile(self, newpass):
        
        Accessfile = open(self.Access_Account_Credentials_FilePath, "r")
        Dumpfile = open(self.Dump_Account_Exceptions_FilePath, "a")

        Num = 1
        self.browser.get(self.URL)
        for line in Accessfile:
            username = line.strip().split(";")[0]
            password = line.strip().split(";")[1]
            
            print(Num, end="")
            print(") USERNAME:= " + username + "   PASSWORD:= " + password+"  ...", end="")
            if(self.run(username, password, newpass, "single") == True):
                print(" NEW PASSWORD:= " + newpass + "....✔\n")

            else:
                Dumpfile.write("\n" + username+";"+password)
                print("....X\n")

            Num = Num + 1
            
        Accessfile.close()
        Dumpfile.close()

    def close(self):
        self.browser.quit()




#UTILITY FUNCTIONS DEFINED HERE

def clear():
    print("\033c")

def cursor(X, Y):
    position = "\033[" + str(Y) + ";" + str(X) + "H"
    print(position, end="")

def rgb(r, g, b, text):
    return f'\x1b[38;2;{r};{g};{b}m{text}\x1b[0m'