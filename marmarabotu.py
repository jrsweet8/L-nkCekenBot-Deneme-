from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from sifreee import usernamee , passwordd
import a 


class marmara : 
    def __init__(self, usernamee , passwordd):
        self.browser = webdriver.Chrome(executable_path="C:/Users/jrswe/Desktop/python_dosyasi/dneme/chromedriver.exe")
        self.username = usernamee
        self.password = passwordd

    def giris(self):
        self.browser.get("https://lms.uzem.marmara.edu.tr/Account/LoginBefore")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='UserName']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='btnLoginName']").click()
        self.browser.find_element_by_xpath("//*[@id='Password']").send_keys(self.password)
        self.browser.find_element_by_xpath("//*[@id='btnLoginPass']").click()
        time.sleep(1)
    def dersleregiris(self):
        self.browser.find_element_by_xpath("//*[@id='r_menu_my_courses']/a/span").click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='courses']/table/tbody/tr/td[1]/a").click()
        time.sleep(1)

    
    def mevzu(self):
    #bu fonksyon kisaltilabilir ama ben yapamadim.
        dersler=[]
        anahtar = input("Linkini istediginiz videonun benzersiz kelimesini girin")
        list = self.browser.find_elements_by_partial_link_text(f"{anahtar}")
        for i in list:
            dersler.append(i.text)
        print(dersler)    
        for x in dersler:
            a = x
            print(a)
            self.browser.find_element_by_partial_link_text(f"{a}").click()
            time.sleep(2.5)
            
            b = self.browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div[6]/a")
            c = (b.get_attribute('href'))
            with open("linkler.txt","a",encoding="UTF-8")as file:
                file.write(f"{a}  dersinin linki:\n  {c}\n\n")

            self.browser.find_element_by_xpath("//*[@id='btnBack']/span").click()
            time.sleep(2.5)


    
    
    
    
    #linkler = []

    #ders = self.browser.find_element_by_xpath("")





basla = marmara(usernamee,passwordd)
basla.giris()
basla.dersleregiris()
basla.mevzu()
