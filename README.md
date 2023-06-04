# What is this

Blender Add-on to mint your render on [Mintbase](https://mintbase.xyz) and upload sources on the [Varda Vault](https://vault.varda.vision) for your collectors
Please check to my introduction video for a detailed how to, or read on.

This module leverages the [near protocol API](https://github.com/near/near-api-py) on the [Blender UI](https://blender.org).

Earendil is a collab between the Mintbase and the Varda DEV team to allow minting and locking secret content to your mintbase NFT.
For a visual introduction, please watch the [announcement video](https://www.youtube.com/coming-soon).

You can either grab the file from here on GitHub, or alternatively on [Gumroad](https://jeeltcraft.gumroad.com/).

# How to
If you don't wanna see the video how to you can go on here.

To install the Near Python API on blender you will need to install a few external modules.
The complete list is on the requirements.txt file on this repo, you can use it to install the modules with pip:

`$ pip install -r requirements.txt`

Then import into blender as explained in the [GC figures how to](https://youtu.be/DSRha-8Zk8w). 
To run the near API script you need to [download it](https://github.com/near/near-api-py) and add the directory on the script\modules folder (I'm using windows here)

`C:\Users\user\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\modules`

If you're on OSX you can find the script folder on the Blender interface, Edit menu -> User preferences -> File Paths -> Scripts

To finally install our Addon you just open the user prefernces: Edit menu -> User Preferences and click on the install (from file) button on the upper right, select the earendill.1.0.0.zip file you downloaded from this repo or from gumroad then you get a panel "Mintbase" on the 3D viewer when you push the N key.

You can use that panel to mint an NFT on your Mintbase store and attach unlockable secret content to it, please configure your store/smart contract on Mintbase before using our tool:

_Setup the minters addresses allowance
_pay GAS

You need to add Title, Description and number of copies directly on this minting interface.

We suggest to use https://nft.storage to store your files and add the urls of your render file (render) and unlockable secret file (source) in the panel before clicking "Mint", once you do you'll be prompted to login to NEAR in a new Chrome window, this plugin only works on chrome and doesn't allow you to keep the keypair in you computer memory for security purposes, so each time you mint you will be prompted with a new passphrase request.

Once you enter the passphrase the addon gets the keypair and if your near address is a store minted and has enough near for the GAS it will mint your NFT on the mintbase store.

You will need to go to the mintbase UI to list your NFT for sale and setup the royalties.

# Reach out
For more information on the thought process behind Earendill, please open an issue on this repo.
