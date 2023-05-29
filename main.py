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
    account = near_api.account.Account(near_provider, signer, signer_id)
    tknmeta = {"title": "Schema", "description": "HUD schematics of dragon Robot",
               "media": "https://cdn.discordapp.com/attachments/1054684309925134356/1087279480281763922/jilt_robot_dragon_led_screen_HUD_schematics_58275ed9-9580-4571-9ae7-a9201223c74e.png"}
    args = {"owner_id": signer_id, "num_to_mint": 1, "metadata": tknmeta, "royalty_args": None,
            "split_owners": None }
    gas = 200000000000000

    amount = 200000000000000

    # Print the private key
    print("\nPrivate Key: " + private_key)
    # Mint action call
    account.function_call(contract_id, "nft_batch_mint", args, gas, amount)
    print("minted!")


# Get the near address from user
addrss = input("Please enter the near address\n==> ")

# Open the chrome browser (install chromedriver if required)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the near wallet url
driver.get(NEAR_WALLET_URL)

# Get the key
time.sleep(60)
private_key = get_private_key(driver, addrss)

mint_render(addrss, private_key)

# check all owned NFTs with gaming API
api_url = "https://api.varda.vision/owner/"+ addrss
response = requests.get(api_url)
raw_nfts = response.json()
print(private_key)

findId = raw_nfts[-1]
fixId = next(fid for fid in findId)

#gather info for new unlockable
token_id = fixId["token_id"]
unlock = "tttttttttt"

#connect unlockable

lock_url = "https://api.varda.vision/new/"+ token_id +"/8/"+ unlock +"/"
headers = {"authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
lockponse = requests.post(lock_url, headers=headers)
lock_nft = lockponse.status_code
print(lock_nft)

# Wait for confirmation from user
input("\nPress enter to exit\n")

# Quit the browser. This is very important because 
# without it there can be memory leaks
driver.quit()
