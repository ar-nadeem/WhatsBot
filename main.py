from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os,sys
import time
from bs4 import BeautifulSoup


class Whatsbot:
    def __init__ (self):

        chrome_options = webdriver.ChromeOptions() 
        chrome_options.add_argument("user-data-dir={}".format(os.path.join(sys.path[0], "chrome-data"))) 
        self.driver = webdriver.Chrome(options=chrome_options,executable_path="chromedriver.exe")
        self.driver.get('https://web.whatsapp.com')
        #Handle logging in
        while 1:
            try:
                elem = self.driver.find_element_by_class_name("landing-main")
            except NoSuchElementException:
                break


        print("Logged in")
        time.sleep(5)

    def Get_Recent_Messages(self):

        new = False

        elem = self.driver.find_elements_by_class_name("FqYAR")

        for e in elem:
            text = e.get_attribute('innerHTML')

            if new == False:
                new = True
                print("Name: {}".format(text))
            else:
                new = False
                print("Message: {}\n".format(text))


        # raw_html=elem[2].get_attribute('innerHTML')
        # print(raw_html)


        #soup = BeautifulSoup(raw_html,'html.parser')
        #print(soup.prettify())

    def Click_On_Chat(self,name):
        elem = self.driver.find_elements_by_class_name("FqYAR")
        for e in elem:
            text = e.get_attribute('innerHTML')

            if (text == name):
                elem = e
                break

        elem.click()

    def Send_Message(self,name,msg):
        # Get the element of the given Name and click it
        self.Click_On_Chat(name)

        time.sleep(1)
        elem = self.driver.find_elements_by_class_name("_13NKt")
        elem = elem[1]
        elem.click()
        elem.clear()
        elem.send_keys(msg)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)



    def Read_Last_Message(self,name):
        self.Click_On_Chat(name)
        elem = self.driver.find_elements_by_class_name("_1Gy50")
        elem = elem[len(elem)-1]

        raw_html = elem.get_attribute('innerHTML')
        soup = BeautifulSoup(raw_html,'html.parser')
        
        return soup.text

    def Set_Reminder(self,name,msg):
        msgg  = msg[msg.find('"'):]
        msgg = msgg[:msgg.find('"')]


        

        pass

    def Tag_All(self,name,msg):
        self.Click_On_Chat(name)
        time.sleep(1)
        elem = self.driver.find_elements_by_class_name("_13NKt")
        elem = elem[1]
        elem.click()
        elem.clear()
        for x in range(10):
            elem.send_keys("@")
            for i in range(x):
                elem.send_keys(Keys.ARROW_DOWN)
            elem.send_keys(Keys.TAB)

        if msg !="":
            elem.send_keys(" ")
            elem.send_keys(msg)
        elem.send_keys(Keys.RETURN)


bot = Whatsbot()

while 1:
    gname = "Sab SCENE"
    text = bot.Read_Last_Message(gname)

    if text == "!?":
        bot.Send_Message(gname,"!potty | !setr")
    if text == "!potty":
        bot.Send_Message(gname,"RAFAY POTTY RAFAY POTTY")
    if text[:5] == "!setr":
        bot.Send_Message(gname,"Setting reminders will be added soon. Abhi mereko Dota khelny")
    if text == "200kg":
        bot.Send_Message(gname,"Hammad Sammandar")
    if text == "5 foot":
        bot.Send_Message(gname,"Sarim Sabeeh")
    if text == "Chicken legs":
        bot.Send_Message(gname,"Leo")
    if text[:4] == "@all":
        bot.Tag_All(gname,text[5:])