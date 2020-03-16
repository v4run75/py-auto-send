import time
import urllib.parse
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import tkinter
from tkinter import *
from tkinter import filedialog
import pandas as pd


def getCSV():
    global df
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv(import_file_path)


# data = pd.read_csv(r'C:\Users\WPS-129\Desktop\db.csv')
# data = pd.DataFrame(df, columns=['Number'])
# print(data)
# getCSV()
# print(df.values.tolist())
# exit()


window = tkinter.Tk()
window.title("Automate WhatsApp")

lbl = Label(window, text="Hello User, Please enter message and upload CSV with names and numbers ",
            font=("Arial Bold", 10))
lbl.grid(column=0, row=0)


lbl = Label(window, text="Message", font=("Arial Bold", 10))
lbl.grid(row=2, column=0)
e2 = Entry(window)
e2.grid(row=2, column=1)

class CloseListener(AbstractEventListener):
    def before_close(self, driver):
        print("tttt")

    def after_close(self, driver):
        print("before_close")
        exit()

    def before_quit(self, driver):
        print("before_quit")

    def after_quit(self, driver):
        print("after_quit")
        exit()

    def on_exception(self, exception, driver):
        print("on_exception")


def sendMessage():
    message = e2.get()
    getCSV()

    numberArray = df.values.tolist()

    print(numberArray[0])
    dicti = dict(numberArray)
    keys = list(dicti.keys())
    values = list(dicti.values())

    driver = webdriver.Chrome("C:/Users/WPS-129/Downloads/chromedriver.exe")
    edriver = EventFiringWebDriver(driver, CloseListener())

    for j in range(len(dicti)):
        if (j == 0):
            edriver.get('https://api.whatsapp.com/send?phone=91' + str(values[j]) + '&text=' +
                       urllib.parse.quote(keys[j] + " " + message))
        else:
            link = 'https://api.whatsapp.com/send?phone=91' + str(values[j]) + '&text=' + urllib.parse.quote(
                keys[j] + " " + message)
            edriver.execute_script("window.open('" + link + "','_blank');")
            tabs = edriver.window_handles
            edriver.switch_to.window(tabs[j])

        user = edriver.find_element_by_id('action-button')
        user.click()

        if (j == 0):
            time.sleep(15)

        time.sleep(8)

        try:
            if (edriver.find_element_by_class_name('_3RiLE')):
                print("Error")
                continue
        except NoSuchElementException:
            print("Continued")

        if (j == 0):
            input('Login check from console')

        time.sleep(8)
        button = edriver.find_element_by_class_name('_3M-N-')
        button.click()

        if (j + 1) < len(numberArray):
            continue
        else:
            print("Finished all tasks")
            exit()


btn = Button(window, text="Submit", command=sendMessage)
btn.grid(column=1, row=7)

window.geometry('600x150')

window.mainloop()
