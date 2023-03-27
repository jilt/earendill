# Import the required modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Import the near_api module from local folder
import near_api

# Import http requests and json utilities to lock the main file
import requests
import json
from types import SimpleNamespace

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

def mint_render(addrss, private_key):
    contract_id = "jiltverse.mintbase1.near"
    signer_id = addrss
    signer_key = private_key
    near_provider = near_api.providers.JsonProvider("https://rpc.near.org")
    key_pair = near_api.signer.KeyPair(signer_key)
    signer = near_api.signer.Signer(signer_id, key_pair)
    account = near_api.account.Account(near_provider, signer)
    tknmeta = {"title": "Schema", "description": "HUD schematics of dragon Robot",
               "media": "https://cdn.discordapp.com/attachments/1054684309925134356/1087279480281763922/jilt_robot_dragon_led_screen_HUD_schematics_58275ed9-9580-4571-9ae7-a9201223c74e.png"}
    args = {"owner_id": account, "num_to_mint": 1, "metadata": tknmeta, "royalty_args": None,
            "split_owners": None }

    # Print the private key
    print("\nPrivate Key: " + private_key)
    # Mint action call
    account.function_call(contract_id, "nft_batch_mint", args)
    print("minted!")

def locker():
    # get owned NFTs after minting
    signer_id = addrss
    api_url = "https://api.varda.vision/owner/" + addrss
    response = requests.get(api_url)
    response.json()

    # transform json into object and select only the most recent entry
    x = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))

    token_id = x.token_id[0]

    # upload new unlockable to API

    unlockable = "url to online file"
    headers = {"Content-Type": "application/json", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibW9oIiwiaWF0IjoxNjc0NDk1OTgxLCJleHAiOjE2NzcwODc5ODF9.oFUCWWymeS_XPac4udgrAhC2ha-ud0KPjkDN8oIoXf8"}
    lock_url = "https://api.varda.vision/new/" + token_id +"/ /" + unlockable
    response = requests.post(lock_url, headers=headers)
    print(response.status_code)


# Get the near address from user
addrss = input("Please enter the near address\n==> ")

# Open the chrome browser (install chromedriver if required)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the near wallet url
driver.get(NEAR_WALLET_URL)

# Get the key
#private_key = get_private_key(driver, addrss)


# If the key does not exist wait for it
#if not private_key:
#    print("\nPrivate Key not found\nPlease log in")
#    while not private_key:
#        time.sleep(1.5)
#        private_key = get_private_key(driver, addrss)
#        minted = mint_render(addrss, private_key)

async def mint():
    try:
        v = await get_private_key(driver, addrss)
    except Exception:
        print("\nPrivate Key not found\nPlease log in")
    await mint_render(addrss, v)


# Wait for confirmation from user
input("\nPress enter to exit\n")

# Quit the browser. This is very important because 
# without it there can be memory leaks
driver.quit()
mint()
