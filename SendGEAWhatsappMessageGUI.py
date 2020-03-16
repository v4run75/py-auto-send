import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Automate Whatsapp")

lbl = Label(window, text="Hello User, Please Enter Name, List of mobile number separated by ',' ",
            font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

lbl = Label(window, text="Name", font=("Arial Bold", 10))
lbl.grid(row=1, column=0)
e1 = Entry(window)
e1.grid(row=1, column=1)

lbl = Label(window, text="Number List(comma separated)*", font=("Arial Bold", 10))
lbl.grid(row=2, column=0)
e2 = Entry(window)
e2.grid(row=2, column=1)


def sendMessage():
    numberList = e2.get()
    numberArray = numberList.split(',')
    driver = webdriver.Chrome("C:/Users/WPS-129/Downloads/chromedriver.exe")

    for j in range(len(numberArray)):
        if (j == 0):
            driver.get('https://api.whatsapp.com/send?phone=91' + numberArray[
                j] + '&text=Hey%2C%20%20%0A%0AWe%2C%20Global%20Excellence%20Awards%20has%20been%20established%20by%20Brand%20Empower%20Pvt.%20Ltd.%20to%20recognize%20the%20various%20companies%2C%20entrepreneurs%20%26%20service%20providers%20for%20their%20outstanding%20performance%20and%20achievements%20in%20their%20respective%20field.%0A%0AGlobal%20Excellence%20Awards%202019%20with%20Chief%20Guest%20Mrs.%20Madhuri%20Dixit%20on%2012th%20Oct%20in%20Mumbai.%20%0A%0AWatch%20Promo%3A%20https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DusvZxp9aZs8%0A%0AThis%20is%20going%20to%20be%20a%20high%20profile%20Event%20in%20Mumbai%20on%2012th%20Oct%202019%2C%20We%20are%20offering%20Partnership%2FSponsorship%2FCo-Sponsorship%20OR%20Get%20awarded%20for%20your%20excellence%20in%20your%20respective%20field.%0A%0AParticipation%20fee%20applied.%20Hurry%2C%20last%20few%20entries%20left.%20Closing%20soon.%20%0A%0AVisit%20us%20%3A%20https%3A%2F%2Fwww.globalexcellenceawards.org%2F%0A%0A%0AThanks%20%26%20Regards%0ABrand%20Empower%0A%2B91%209667227084')
        else:
            link = 'https://api.whatsapp.com/send?phone=91' + numberArray[
                j] + '&text=Hey%2C%20%20%0A%0AWe%2C%20Global%20Excellence%20Awards%20has%20been%20established%20by%20Brand%20Empower%20Pvt.%20Ltd.%20to%20recognize%20the%20various%20companies%2C%20entrepreneurs%20%26%20service%20providers%20for%20their%20outstanding%20performance%20and%20achievements%20in%20their%20respective%20field.%0A%0AGlobal%20Excellence%20Awards%202019%20with%20Chief%20Guest%20Mrs.%20Madhuri%20Dixit%20on%2012th%20Oct%20in%20Mumbai.%20%0A%0AWatch%20Promo%3A%20https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DusvZxp9aZs8%0A%0AThis%20is%20going%20to%20be%20a%20high%20profile%20Event%20in%20Mumbai%20on%2012th%20Oct%202019%2C%20We%20are%20offering%20Partnership%2FSponsorship%2FCo-Sponsorship%20OR%20Get%20awarded%20for%20your%20excellence%20in%20your%20respective%20field.%0A%0AParticipation%20fee%20applied.%20Hurry%2C%20last%20few%20entries%20left.%20Closing%20soon.%20%0A%0AVisit%20us%20%3A%20https%3A%2F%2Fwww.globalexcellenceawards.org%2F%0A%0A%0AThanks%20%26%20Regards%0ABrand%20Empower%0A%2B91%209667227084'
            driver.execute_script("window.open('" + link + "','_blank');")
            tabs = driver.window_handles
            driver.switch_to.window(tabs[j])

        user = driver.find_element_by_id('action-button')
        user.click()

        if (j == 0):
            time.sleep(15)

        time.sleep(8)

        try:
            if (driver.find_element_by_class_name('_3RiLE')):
                print("Error")
                continue
        except NoSuchElementException:
            print("Continued")

        if (j == 0):
            input('Login check from console')

        time.sleep(8)
        button = driver.find_element_by_class_name('_3M-N-')
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

# numberList = "7838342614,9667227084,9911545588,9910505554,7838342615,7838342613"
# numberArray = numberList.split(',')
# driver = webdriver.Chrome("C:/Users/WPS-129/Downloads/chromedriver.exe")
#
# for j in range(len(numberArray)):
#     if (j == 0):
#         driver.get('https://api.whatsapp.com/send?phone=91' + numberArray[
#             j] + '&text=Hey%2C%20%20%0A%0AWe%2C%20Global%20Excellence%20Awards%20has%20been%20established%20by%20Brand%20Empower%20Pvt.%20Ltd.%20to%20recognize%20the%20various%20companies%2C%20entrepreneurs%20%26%20service%20providers%20for%20their%20outstanding%20performance%20and%20achievements%20in%20their%20respective%20field.%0A%0AGlobal%20Excellence%20Awards%202019%20with%20Chief%20Guest%20Mrs.%20Madhuri%20Dixit%20on%2012th%20Oct%20in%20Mumbai.%20%0A%0AWatch%20Promo%3A%20https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DusvZxp9aZs8%0A%0AThis%20is%20going%20to%20be%20a%20high%20profile%20Event%20in%20Mumbai%20on%2012th%20Oct%202019%2C%20We%20are%20offering%20Partnership%2FSponsorship%2FCo-Sponsorship%20OR%20Get%20awarded%20for%20your%20excellence%20in%20your%20respective%20field.%0A%0AParticipation%20fee%20applied.%20Hurry%2C%20last%20few%20entries%20left.%20Closing%20soon.%20%0A%0AVisit%20us%20%3A%20https%3A%2F%2Fwww.globalexcellenceawards.org%2F%0A%0A%0AThanks%20%26%20Regards%0ABrand%20Empower%0A%2B91%209667227084')
#     else:
#         link = 'https://api.whatsapp.com/send?phone=91' + numberArray[
#             j] + '&text=Hey%2C%20%20%0A%0AWe%2C%20Global%20Excellence%20Awards%20has%20been%20established%20by%20Brand%20Empower%20Pvt.%20Ltd.%20to%20recognize%20the%20various%20companies%2C%20entrepreneurs%20%26%20service%20providers%20for%20their%20outstanding%20performance%20and%20achievements%20in%20their%20respective%20field.%0A%0AGlobal%20Excellence%20Awards%202019%20with%20Chief%20Guest%20Mrs.%20Madhuri%20Dixit%20on%2012th%20Oct%20in%20Mumbai.%20%0A%0AWatch%20Promo%3A%20https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DusvZxp9aZs8%0A%0AThis%20is%20going%20to%20be%20a%20high%20profile%20Event%20in%20Mumbai%20on%2012th%20Oct%202019%2C%20We%20are%20offering%20Partnership%2FSponsorship%2FCo-Sponsorship%20OR%20Get%20awarded%20for%20your%20excellence%20in%20your%20respective%20field.%0A%0AParticipation%20fee%20applied.%20Hurry%2C%20last%20few%20entries%20left.%20Closing%20soon.%20%0A%0AVisit%20us%20%3A%20https%3A%2F%2Fwww.globalexcellenceawards.org%2F%0A%0A%0AThanks%20%26%20Regards%0ABrand%20Empower%0A%2B91%209667227084'
#         driver.execute_script("window.open('" + link + "','_blank');")
#         tabs = driver.window_handles
#         driver.switch_to.window(tabs[j])
#
#     user = driver.find_element_by_id('action-button')
#     user.click()
#
#     if(j==0):
#         time.sleep(15)
#
#     time.sleep(8)
#
#     try:
#         if(driver.find_element_by_class_name('_3RiLE')):
#             print("Error")
#             continue
#     except NoSuchElementException:
#             print("Continued")
#
#     if (j == 0):
#         input('Login check from console')
#
#     time.sleep(8)
#     button = driver.find_element_by_class_name('_3M-N-')
#     button.click()
#
#     if (j + 1) < len(numberArray):
#         continue
#     else:
#         print("Finished all tasks")
#         exit()
