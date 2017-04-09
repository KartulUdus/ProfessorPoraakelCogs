# [WIP] CheckForced

This cog allows to check against /plfe/version to determine the current API version Niantic requires to connect to PoGo.

If the IP address of the system running Red is banned, you will need to install a proxy with this cog using the instructions below.

Setup Instructions (if the system IP address is banned):
* Install the cog using Red's downloader, or by downloading the .py and placing it in your Red's cogs folder.
* Disable the CheckForced cog if it was automatically enabled.
* Open CheckForced.py in Red's cogs folder, and at line 17, between the '' of https: '', place the IP address and port of your proxy. Ex: `'https': '101.8.101.91:3128'`
* Save the .py file, and enable the CheckForced cog.
* Test with !checkforced
