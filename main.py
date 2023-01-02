# Import the required modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Import the near_api module from local folder
import near_api


# The URL for the near wallet
NEAR_WALLET_URL = "https://wallet.near.org/"

# The format for the key in local storage
KEY_FMT = "nearlib:keystore:{addrss}:default"

# This is the variable that will contain the private key if found
private_key = None

def get_private_key(driver, addrss):
    '''Function to get the value for the key from local storage. 
    Returns None if key does not exist yet'''
    key = KEY_FMT.format(addrss=addrss)
    return driver.execute_script(f'return window.localStorage.getItem("{key}")')

# Get the near address from user
addrss = input("Please enter the near address\n==> ")

# Open the chrome browser (install chromedriver if required)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the near wallet url
driver.get(NEAR_WALLET_URL)

# Get the key
private_key = get_private_key(driver, addrss)

# If the key does not exist wait for it
if not private_key:
    print("\nPrivate Key not found\nPlease log in")
    while not private_key:
        time.sleep(0.5)
        private_key = get_private_key(driver, addrss)

# Print the private key
print("\nPrivate Key: " + private_key)

# Wait for confirmation from user
input("\nPress enter to exit\n")

# Quit the browser. This is very important because 
# without it there can be memory leaks
driver.quit()