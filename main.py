import tkinter

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tkinter import *

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


def on_closing():
    # Code to be run when the window is closed
    root.destroy()
    driver.quit()


def update_clock():
    # Update the clock here
    if hacks:
        try:
            selected_elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'Input_input__') and @value='']")
            for i in selected_elements:
                text_element = i.find_element(By.XPATH, "../preceding-sibling::span/span")
                i.send_keys(text_element.get_attribute("innerHTML"))
        except:
            driver.quit()
            root.destroy()
            return 1
    # Schedule the function to be called again in 1 second
    root.after(200, update_clock)


def update_hacks():
    global hacks
    global lbl
    hacks = not hacks
    if hacks:
        lbl.config(text="Hacks ON")
    else:
        lbl.config(text="Hacks OFF")


root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
hacks = tkinter.BooleanVar()

root.title("Seneca Hacks")
root.minsize(250, 100)
root.maxsize(250, 100)
root.iconbitmap("Icon/favicon.ico")

driver.get("https://app.senecalearning.com/courses")
# driver.implicitly_wait(5)

lbl = Label(root, font=10)
lbl.pack()
button = Checkbutton(root, variable=hacks, command=update_hacks)
button.pack()


update_hacks()

update_clock()

root.mainloop()
