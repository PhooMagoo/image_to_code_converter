### Loop through a folder and create <asp:Image> elements out of every
### picture found. Copy them to the clipboard for ease of use.

# TODO: Nothing. I thiiiink it works exactly how I wanted it to.

import os           # For looping through the folder.
import pandas as pd # For saving to teh clipboard.

items = []      # List used for constructing image URL.
elements = []   # List for combining everything together.
number = 1      # The number we'll use to increment the image element's ID.

# Create our source variable.
source = r''
source = input(r'Enter folder to scan: ')

# Provide an abbreviation of the game's name for the image's ID.
abbreviation = r''
abbreviation = input(r'Enter the abbreviation for the game: ')

# Split up the source to just be the items we need.
split = source.split("\\")

# Construct the beginning of the src.
url = '~/' + split[-3] + '/' + split[-2] + '/' + split[-1] + '/'

# Loop through all of the images in the provided directory.
for root, dirs, files in os.walk(source):
    try:
        for f in files:             # For every file...
            items.append(url + f)   # Combine URL and f into a final usable URL.
    except Exception as e:
        print(e + " : " + f)

# Loop through every URL we've managed to snag...
for item in items:
    try:
        # Create our <asp:Image> elements and append them to our list.
        elements.append(r'<asp:Image ID="img' + abbreviation + str(number) + '" CssClass="image" runat="server" ImageUrl="' + item + '" />') # Create the HTML element.
        number = number + 1 # Increment the number for the filename ID.
    except Exception as e:
        print(e + ' : ' + item)

# Copy all of the finalized HTML elements to the clipboard.
pd.DataFrame(elements).to_clipboard(excel=False, header=False, index=False)
    
