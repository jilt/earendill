# What is this

Blender Add-on to mint your render on [Mintbase](https://mintbase.xyz) and upload sources on the [Varda Vault](https://vault.varda.vision) for your collectors
Please check to my introduction video for a detailed how to, or read on.

This module leverages the [near protocol API](https://github.com/near/near-api-py) on the [Blender UI](https://blender.org).

Earendil is a collab between the Mintbase and the Varda DEV team to allow minting and locking secret content to your mintbase NFT.
For a visual introduction, please watch the [announcement video](https://www.youtube.com/coming-soon).

You can either grab the file from here on GitHub, or alternatively on [Gumroad](https://jeeltcraft.gumroad.com/).

# Get Started
If you don't wanna see the [video how to](https://drive.google.com/file/d/1V16mFIFiAzmUCBNMxqhbQIw5otaX-5Cn/view?usp=drivesdk) you can go on here.

To run the Near Python API on blender you will need to install a few external modules.
The complete list is on the requirements.txt file on this repo, you can use it to install the packages with pip:

`$ pip install -r requirements.txt`

If you don't wanna install python on your PC (considering that Blender already has its own python version running internally) [here](https://drive.google.com/file/d/1-XbegCJa4DW3rfJ2l3-8YlczOgRMx85t/view?usp=drive_link) is a zipped version of the site-package folder with all the needed libraries, you can unzip that and place it on:

`C:\Program Files\Blender Foundation\Blender 3.5\3.5\python\lib\site-packages`

Then import into blender as explained in the [GC figures how to](https://youtu.be/DSRha-8Zk8w).

I'm committed to keeping the download package updated for the next year.

To run the near API script you need to [download it](https://github.com/near/near-api-py) and add the directory on the script\modules folder (windows path here)

`C:\Users\user\AppData\Roaming\Blender Foundation\Blender\3.5\scripts\modules`

If you are running windows 10 you may need to run the selenium package (find it in the [site-packages link](https://drive.google.com/file/d/1-XbegCJa4DW3rfJ2l3-8YlczOgRMx85t/view?usp=drive_link) i shared above) from this module folder too.

If you're on OSX you can find the script folder on the Blender interface, Edit menu -> User preferences -> File Paths -> Scripts

Finally, to install our Addon you just open the user preferences: Edit menu -> User Preferences and click on the install (from file) button on the upper right, select the earendill.1.0.0.zip file you downloaded from this repo or from gumroad then you get a panel "Mintbase" on the 3D viewer when you push the N key.

You can use that panel to mint an NFT on your Mintbase store and attach unlockable secret content to it, please configure your store/smart contract on Mintbase before using our tool:

1) Setup the minters addresses allowance
2) Pay GAS

You need to add Title, Description and number of copies directly on our minting interface.

We suggest to use https://nft.storage to store your files and add the urls of your render file (render) and unlockable secret file (source) in the panel before clicking "Mint", once you do you'll be prompted to login to NEAR in a new Chrome window, this plugin only works on chrome and doesn't allow you to keep the keypair in you computer memory for security purposes, so each time you mint you will be prompted with a new passphrase request.

Once you enter the passphrase the addon gets the keypair and if your near address is a store minter and has enough near for the GAS it will mint your NFT on the mintbase store.

You will need to go to the [mintbase UI](https://mintbase.xyz) to list your NFT for sale and setup royalties.

Your collectors will need to go to the [Varda vault](https://vault.varda.vision) to get the source file or unlockable content you decided to attaxh to your NFT.

Happy creation

# Reach out
For more information on the thought process behind Earendill, please open an issue on this repo.
