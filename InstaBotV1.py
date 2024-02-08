from Robot import *
import os
import json



COMMON_PASS = None

def Home():
    while(True):
        clear()
        print(rgb(20, 240, 0, "[E]<-- Back/Exit                   INSTAGRAM AUTOMATION SOFTWARE Version 1.0")+"\n\n\n")

        print("Select an option\n")
        print("[1] Run InstaBot    [2] Set Faulty Account File path   [3] Set common password  [4] Set Fresh Account File path\n\n")

        

        while(True):
            print(rgb(255, 105, 180, "\n\ninput>>"), end="")
            option = input()

            if(option == "1"):
                StartInstaBot()
                break

            elif option == "2":
                UnprocessedAccounts()
                break
        
            elif option == "3":
                SetPassword()
                break
                
            elif option == "4":
                demp()
            
            elif option == "E" or option == "e":
                return
            

    return


def StartInstaBot():

    print(rgb(240, 10, 10, "\n\n[ALERT]: Confirm to proceed to run InstaBot\n"))
    print(rgb(10, 140, 10, "(Y)  Confirm"))
    print(rgb(110, 110, 110, "(E)  Exit/back"))
    
    
    while(True):
        option = input()

        if(option == "Y" or option == "y"): break
        if(option == "E" or option == "e"): return False
        else: continue
    
    JsonFile = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "r")
    Bot = json.load(JsonFile)
    JsonFile.close()

    password = Bot["Bots"][0]["CommonPassword"]
    Accessfile = Bot["Bots"][0]["InputFilePath"]
    DumpFilePath = Bot["Bots"][0]["DumpFilePath"]

    
    Bot = INSTABOT()
    Bot.SpecifyFilePath(Accessfile, DumpFilePath)
    Bot.runfile(password)
    Bot.close()

    print("\nFinished, more details about exceptions in option [2]")
    print("Enter E or e to exit or select any option")
    
    B = input()


def UnprocessedAccounts():
    
    JsonFile = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "r")
    Bot = json.load(JsonFile)
    JsonFile.close()
    
    print("\ncurrent path = " + Bot["Bots"][0]["DumpFilePath"], end="")
    print("\n\ntype the new file path = ", end="")
    path = input()
    
    if(path == "e" or path == "E"): return False
   
    JsonFile = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "w")
    Bot["Bots"][0]["DumpFilePath"] = path
    json.dump(Bot, JsonFile, indent=2)
    JsonFile.close()



def SetPassword():
    print(rgb(240, 10, 10, "[WARNING]: InstaBot will set this password for all the accounts when run"))
    print(rgb(240, 10, 10, "           You would have to RE-RUN the InstaBot in case to replace with new"))
    

    JsonFile = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "r")
    Bot = json.load(JsonFile)
    JsonFile.close()

    Password = Bot["Bots"][0]["CommonPassword"]
    print(rgb(200, 200, 10, "\nCurrent Password = [" + Password + "]"))
    
    print(rgb(10, 200, 10, "\n\nENTER NEW PASSWORD >> "), end="")
    newpass = input()
    
    
    if(newpass == "E" or newpass == "e"): return False
    
    Bot["Bots"][0]["CommonPassword"] = newpass
    JsonFile = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "w")
    json.dump(Bot, JsonFile, indent=2)
    JsonFile.close()
    print("\nNEW PASSWORD is = " + newpass)

    return True

    B = input()


def demp():
    JsonFile = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "r")
    Bot = json.load(JsonFile)
    #JsonFile.close()
    
    print("\ncurrent path = " + Bot["Bots"][0]["InputFilePath"], end="")
    print("\n\ntype the new file path for fresh = ", end="")
    path = input()
    
    if(path == "e" or path == "E"): return False
   
    JsonFile = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "w")
    Bot["Bots"][0]["InputFilePath"] = path
    json.dump(Bot, JsonFile, indent=2)
    JsonFile.close()


Home()


