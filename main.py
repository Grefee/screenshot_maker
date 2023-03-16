from selenium import webdriver
import time
import os
import pathlib


class ScreenShot:
    def readConfig():
        global webLink
        with open("config.txt", "r") as f:
            lines = f.readlines()
            webLink = lines[0]
            print(webLink)

            
    def openChrome():
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                                  options=options)

        site = webLink
        driver.get(site)
        
        time.sleep(8)

        
    def makeBuffScreen():
        global buffScreen
        buffScreen = r"./screens/BufferScreenshot.png"
        print("new screen made")
        driver.save_screenshot(buffScreen)

        
    def renBuffToScreen():
        old_name = buffScreen
        new_name = r"./screens/Screenshot.png"
        os.rename(old_name, new_name)

        
    def renScreenToOld():
        old_name = r"./screens/Screenshot.png"
        new_name = r"./screens/OldScreenshot.png"
        os.rename(old_name, new_name)

        
    def delOldScreen():
        delPath = './screens/OldScreenshot.png'
        os.remove(delPath)

        
    def clearAllScreens():
        delPath01 = pathlib.Path('./screens/BufferScreenshot.png')
        delPath02 = pathlib.Path('./screens/Screenshot.png')
        delPath03 = pathlib.Path('./screens/OldScreenshot.png')
        if delPath01.exists():
            os.remove(delPath01)
        if delPath02.exists():
            os.remove(delPath02)
        if delPath03.exists():
            os.remove(delPath03)

            
if __name__ == "__main__":
    ScreenShot.readConfig()
    ScreenShot.clearAllScreens()
    ScreenShot.openChrome()
    ScreenShot.makeBuffScreen()
    ScreenShot.renBuffToScreen()
    ScreenShot.makeBuffScreen()
    time.sleep(5)
    while True:
        ScreenShot.renScreenToOld()
        ScreenShot.renBuffToScreen()
        ScreenShot.delOldScreen()
        ScreenShot.makeBuffScreen()
        time.sleep(3)
