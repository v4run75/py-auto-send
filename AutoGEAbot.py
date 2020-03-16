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

lbl = Label(window, text="Hello User Please Enter Your Phone Number and upload CSV",
            font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

lbl = Label(window, text="Your Phone Number(10 digits)", font=("Arial Bold", 10))
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
    phoneNumber = e2.get()
    getCSV()

    numberArray = df.values.tolist()

    print(numberArray)
    dicti = dict(numberArray)
    keys = list(dicti.keys())
    values = list(dicti.values())

    commonURL = "%2C%20%20%0A%0AWe%2C%20Global%20Excellence%20Awards%20has%20been%20established%20by%20Brand%20Empower%20Pvt.%20Ltd.%20to%20recognize%20the%20various%20companies%2C%20entrepreneurs%20%26%20service%20providers%20for%20their%20outstanding%20performance%20and%20achievements%20in%20their%20respective%20field.%0A%0AGlobal%20Excellence%20Awards%202019%20with%20Chief%20Guest%20Mrs.%20Madhuri%20Dixit%20on%2012th%20Oct%20in%20Mumbai.%20%0A%0AWatch%20Promo%3A%20https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DusvZxp9aZs8%0A%0AThis%20is%20going%20to%20be%20a%20high%20profile%20Event%20in%20Mumbai%20on%2012th%20Oct%202019%2C%20We%20are%20offering%20Partnership%2FSponsorship%2FCo-Sponsorship%20OR%20Get%20awarded%20for%20your%20excellence%20in%20your%20respective%20field.%0A%0AParticipation%20fee%20applied.%20Hurry%2C%20last%20few%20entries%20left.%20Closing%20soon.%20%0A%0AVisit%20us%20%3A%20https%3A%2F%2Fwww.globalexcellenceawards.org%2F%0A%0A%0AThanks%20%26%20Regards%0ABrand%20Empower%0A"

    driver = webdriver.Chrome("C:/Users/WPS-129/Downloads/chromedriver.exe")
    edriver = EventFiringWebDriver(driver, CloseListener())

    for j in range(len(dicti)):
        if (j == 0):
            edriver.get('https://api.whatsapp.com/send?phone=91' + str(values[j]) + '&text=' +
                        urllib.parse.quote("Hey, ") + urllib.parse.quote(keys[j]) + commonURL + urllib.parse.quote(
                "+91") + urllib.parse.quote(
                phoneNumber))
        else:
            link = 'https://api.whatsapp.com/send?phone=91' + str(values[j]) + '&text=' + urllib.parse.quote(
                "Hey, ") + urllib.parse.quote(keys[j]) + commonURL + urllib.parse.quote(
                "+91") + urllib.parse.quote(phoneNumber)

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
                f = open("wrong.txt", "a")
                f.write(str(values[j])+"\n")
                f.close()
                continue
        except NoSuchElementException:
            print("Continued")


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
