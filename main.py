from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
import winreg


def get_default_browser():
    # Open the registry key for user-level settings
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice")

    # Read the ProgID (Program ID) value for the default browser
    prog_id, _ = winreg.QueryValueEx(reg_key, "ProgId")

    # Extract the browser name from the ProgID
    browser_name = prog_id.split('.')[-1]

    return browser_name


def run_browser(browser):
    print(browser)
    global options, driver
    if browser == 'ChromeHTML':
        from selenium.webdriver.chrome.options import Options
    elif browser == 'MSEdgeHTM':
        from selenium.webdriver.edge.options import Options
    elif browser.startswith("FirefoxURL"):
        from selenium.webdriver.firefox.options import Options
    else:
        print('ERROR: Browser Not Supported')
        return 1

    options = Options()

    if browser == 'ChromeHTML' or browser == 'MSEdgeHTM':
        options.add_experimental_option("detach", True)
    elif browser.startswith("FirefoxURL"):
        options.set_preference('detach', True)

    if browser == 'ChromeHTML':
        driver = webdriver.Chrome(options=options)
    elif browser == 'MSEdgeHTM':
        driver = webdriver.Edge(options=options)
    elif browser.startswith("FirefoxURL"):
        driver = webdriver.Firefox(options=options)

    driver.get("https://app.senecalearning.com/courses/login")
    driver.maximize_window()


run_browser(get_default_browser())


def on_closing():
    # Code to be run when the window is closed
    root.destroy()
    driver.quit()


def update_clock():
    # Update the clock here
    if len(driver.window_handles) == 0:
        driver.quit()
        root.destroy()
    else:
        if auto:
            try:
                selected_elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'Input_input__') and "
                                                                   "@value='']")
                for i in selected_elements:
                    text_element = i.find_element(By.XPATH, "../preceding-sibling::span/span")
                    i.send_keys(text_element.get_attribute("innerHTML"))
            except:
                root.destroy()
                driver.quit()
                return 1
    # Schedule the function to be called again in 1 second
    root.after(200, update_clock)


def update_auto():
    global auto
    global lbl
    auto = not auto
    if auto:
        lbl.config(text="Auto On")
    else:
        lbl.config(text="Auto Off")


root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
auto = BooleanVar()

root.title("Auto Seneca")
root.minsize(250, 100)
root.maxsize(250, 100)
root.iconbitmap("icon/favicon.ico")

lbl = Label(root, font=10)
lbl.pack()
button = Checkbutton(root, variable=auto, command=update_auto)
button.pack()

update_auto()

update_clock()

root.mainloop()
