from Robot import INSTABOT
from Frame import FRAME
from Textbox import TEXTBOX
from Element import UTILITY
import json
import time


def Inputbox(x, y, w, h, str = ""):
    u = UTILITY()
    u.eraseArea(x, y, w, h)
    inp = ""
    u.cursor(x, y)
    print(str, end="")
    inp = input()
    return inp

def MainScreen():
    #Clear the screen first
    util = UTILITY()
    util.clear()
    
    

    mainframe = FRAME(5, 3, 70, 31)
    bar = FRAME(mainframe.getX(), mainframe.getY() + 5, 15, 21)
    sframe = FRAME(mainframe.getX()+bar.getW() + 6, mainframe.getY() + 3, 44, 25)
    options = TEXTBOX(mainframe.getX() + 2, mainframe.getY() + 8, 29, 10)
   
    #main screen
    mainframe.set_name(" INSTAGRAM AUTOMATION SOFTWARE VERSION 2.17 ", 24)
    mainframe.set_namecolor(200, 40, 80)
    
    #secondary screen
    sframe.set_name(" INPUT & OUTPUT WINDOW ")
    sframe.set_namecolor(40, 100, 50)
    
    #bar
    bar.set_name(" OPTIONS MENU ")
    bar.set_namecolor(40, 50, 150)
    #options screen
    options.write("[1]  BOT 1\n\n")
    options.write("[2]  BOT 2\n\n")
    options.write("[3]  BOT 3\n\n")
    options.write("[4]  Set common password")
    options.draw()
    

    #draw
    bar.draw()
    mainframe.draw()
    sframe.draw()
   
    ibox = TEXTBOX(bar.getX()+1, bar.getY()+13, 26, 1, "input")
    ibox.write("SELECT >> ")
    while(True):

        str = ibox.draw()

        if(str == "e"):
            return 0
        
        elif(str == "1"):
            ibox.erase()
            InstaBot1(sframe.getX()+1, sframe.getY()+2, sframe.getW, 0)
            

        elif(str == "2"):
            pass

        elif(str == "3"):
            pass

        elif(str == "4"):
            InitiateBotProcess(sframe.getX()+1, sframe.getY()+2, sframe.getW, 0)
            pass

        else:
           pass

    

def InitiateBotProcess(x, y, w, h):
    box = TEXTBOX(x, y, 76, 8)
    option = TEXTBOX(x, y+9, 76, 3)
    ibox = TEXTBOX(x+3, y+15, 20, 1, "input")
    ibox.write("\x1b[34mSELECT >> \x1b[0m")
    box.write(" [ALERT]:\n\n")
    box.write(" You must review  the \x1b[31mInputFile, Dumpfile and CommonPassword\x1b[0m\n")
    box.write(" for each BOT, failure to do so will result in program crash.\n")
    box.write(" If you accidentally set wrong password and started BOTs\n")
    box.write(" Program does not keep track of LOGS. Use precaution\n\n")
    box.write(" !DO NOT STRICTLY TOUCH ANY PEICE OF CODE!")
    box.draw()
    
    option.write("[1] RUN BOT 1     [2] RUN BOT 2     [3] RUN BOT 3")
    option.draw()
    
    while(True):

        inp = ibox.draw()
        
        if(inp == "e" or inp == "E"):
            box.erase()
            ibox.erase()
            option.erase()
            return
        

        if(inp == "1"):
            BOT = INSTABOT()

            file = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "r")
            bot = json.load(file)
            file.close()

            inputfile = bot["Bots"][0]["InputFilePath"]
            dumpfile = bot["Bots"][0]["DumpFilePath"]
            password = bot["Bots"][0]["CommonPassword"]
            active = bot["Bots"][0]["RunTimeActive"]

            if(active == "somethingfortest"):
                tbox = TEXTBOX(x+3, y+15, 40, 1)
                tbox.write("   [STATUS = CAN'T RUN WHILE ALREADY RUNNING]")
                tbox.draw()

                h = input()

            if(active == "false"):
                u = UTILITY()
                #Open file and set activity to true to indicate the bot is already running
                #File = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "w")
                #bot["Bots"][0]["RunTimeActive"] = True
                #json.dump(bot, File, indent =2)
                #File.close()
                u.cursor(4, 46)
                BOT.SpecifyFilePath(inputfile, dumpfile)
                BOT.runfile(password)
                BOT.close()

                #Close to indicate bot has finished running
                #File = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "w")
                #bot["Bots"][0]["RunTimeActive"] = False
                #json.dump(bot, File, indent =2)
                #File.close()


        elif(inp == "2"):
            pass

        elif(inp == "3"):
            pass

        else:
            continue


    box.erase()
    pass


def InstaBot1(x, y, w, h):
    box = TEXTBOX(x, y, 76, 8)
    options = TEXTBOX(x, y + 8, 50, 7)
    
    ibox = TEXTBOX(x+3, y+15, 20, 1, "input")

    file = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "r")
    Botdata = json.load(file)
    file.close()

    Botid = str(Botdata["Bots"][0]["BotID"])
    inputfile = Botdata["Bots"][0]["InputFilePath"]
    dumpfile = Botdata["Bots"][0]["DumpFilePath"]
    password = Botdata["Bots"][0]["CommonPassword"]
    active = Botdata["Bots"][0]["RunTimeActive"]
    
    #Status bar
    box.write("   [BOT STATUS]   \n\n")
    box.write("   Bot ID: " + Botid +"\n")
    box.write("   \x1b[31mCurrent password\x1b[0m: [" + password+"]\n")
    box.draw()

    #options  
    while(True):
        options.clear()
        ibox.clear()
        ibox.set_position(x+3, y+15)
        ibox.set_height(1)
        ibox.set_width(20)
        ibox.write("\x1b[35mSELECT >>\x1b[0m ")
        options.write("   [1] Set \x1b[32mINPUT\x1b[0m File Path\n\n")
        options.write("   [2] Set \x1b[33mDUMP\x1b[0m  File Path\n\n")
        options.write("   [3] Set \x1b[34mCOMMON\x1b[0m password")
        options.draw()
        Str = ibox.draw()

        if(Str == "e" or Str == "E"):
                box.erase()
                options.erase()
                return
            
        elif(Str == "1"):
            options.erase()
            ibox.erase()
                
            #Display the current file output
            tbox = TEXTBOX(x+3, y + 8, 50, 7)
            tbox.write("\x1b[32mCURRENT INPUT FILE PATH\x1b[0m:\n")
            tbox.write(inputfile)
            tbox.draw()
                
            ibox.set_width(70)
            ibox.set_height(3)
            ibox.set_position(x+3, y+15)
            ibox.clear()
            ibox.write("Enter new file path : ")
            newfilepath = ibox.draw()
            ibox.erase()

            if(newfilepath == "e" or newfilepath == "E"):
                 continue
                
            file = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "w")
            Botdata["Bots"][0]["InputFilePath"] = newfilepath
            json.dump(Botdata, file, indent =2)
            file.close()
            
            tbox.erase()
            tbox.clear()
            tbox.write("\x1b[32mCURRENT INPUT FILE PATH\x1b[0m:\n")
            tbox.write(newfilepath)
            tbox.draw()
            
            #Update the information
            inputfile = newfilepath

        elif(Str == "2"):
             options.erase()
             ibox.erase()
                #Display the current file output
             tbox = TEXTBOX(x+3, y + 8, 50, 7)
             tbox.write("\x1b[32mCURRENT DUMP FILE PATH\x1b[0m:\n")
             tbox.write(dumpfile)
             tbox.draw()
                    
             ibox.set_width(70)
             ibox.set_height(3)
             ibox.set_position(x+3, y+15)
             ibox.clear()
             ibox.write("Enter new file path : ")
             newfilepath = ibox.draw()
             ibox.erase()

             if(newfilepath == "e" or newfilepath == "E"):
                 continue
                    
             file = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "w")
             Botdata["Bots"][0]["DumpFilePath"] = newfilepath
             json.dump(Botdata, file, indent =2)
             file.close()
                
             tbox.erase()
             tbox.clear()
             tbox.write("\x1b[32mCURRENT DUMP FILE PATH\x1b[0m:\n")
             tbox.write(newfilepath)
             tbox.draw()
                
                #Update the information
             dumpfile = newfilepath
             pass

        elif(Str == "3"):
             options.erase()
             ibox.erase()
          
             ibox.set_width(70)
             ibox.set_height(3)
             ibox.set_position(x+3, y+15)
             ibox.clear()
             ibox.write("Enter new common password: ")
             newpass = ibox.draw()
             ibox.erase()

             if(newpass == "e" or newpass == "E"):
                 continue
                    
             file = open(r"C:\Users\yasha\Bot Automation\InstagramAutomation\Configurations.json", "w")
             Botdata["Bots"][0]["CommonPassword"] = newpass
             json.dump(Botdata, file, indent =2)
             file.close()
                
                
            #Update the information
             password = newpass
             pass


    box.erase()
    options.erase()
   
def Option2():
        
    pass

MainScreen()