"""
    Created by Wallee#8314 / Red-exe-Engineer

    Minecraft Pi Texture Reader Version 1.0

    This program helps with making custom skins
    and armor for texture packs by showing you
    where pieces are located

    Believe me, it is harder than it looks, but
    there is a pattern to it :p
"""

# Imports
import PySimpleGUI as sg
from os import listdir

# Define a search function
def search(items: list, text: str):

    # Create a list for items to append items that match the search
    newItems = []

    # Loop through the items
    for item in items:

        # Check if text is in the current item and that the item is not None.png
        if text.lower() in item[:-4].lower() and not item == "None.png":

            # Append the item to the list of new items
            newItems.append(item[:-4])

    # Sorth the list
    newItems.sort()

    # Reverse, append, and reverse again so None will be at the top
    newItems.reverse()
    newItems.append("None")
    newItems.reverse()

    # Return the list
    return(newItems)

# Use the search function to get all the images in the chars, pants, and armor directories
chars = search(listdir("chars"), "")
pants = search(listdir("pants"), "")
armor = search(listdir("armor"), "")

# Create the window layout
layout = [
    [
        # The main image
        sg.Image("chars/None.png", key="-IMAGE-"),
    ],
    [
        [
            # Skin search
            sg.In(size=(20, 1), enable_events=True, key="-SEARCH-CHARS-"),
            sg.Text(""),

            # Pants search
            sg.In(size=(20, 1), enable_events=True, key="-SEARCH-PANTS-"),
            sg.Text(""),

            # Armor search
            sg.In(size=(20, 1), enable_events=True, key="-SEARCH-ARMOR-")
        ],
        [
            # List the items in the char, pants, and armor directories
            sg.Listbox(chars, size=(20, 22), enable_events=True, key="-CHARS-"),
            sg.Listbox(pants, size=(20, 22), enable_events=True, key="-PANTS-"),
            sg.Listbox(armor, size=(20, 22), enable_events=True, key="-ARMOR-")
        ]
    ]
]

# Create the window
window = sg.Window(title="Minecraft Pi Texture Reader: Version 0.0", layout=[layout], size=(520, 700))

# Loop forever
while True:

    # Get events and values from the window
    event, values = window.read()

    # Check if the user wants to close the window
    if event == sg.WIN_CLOSED:

        # Close the window by exiting the program
        exit()

    # Check if the user has clicked a character sprite
    elif event == "-CHARS-":

        # Update the main image with the spite the user has selected
        window["-IMAGE-"].update("chars/" + values["-CHARS-"][0] + ".png")

    # Check if the user has clicked a leggings sprite
    elif event == "-PANTS-":

        # Update the main image with the sprite the user has selected... again
        window["-IMAGE-"].update("pants/" + values["-PANTS-"][0] + ".png")

    # Check if the user has clicjed an armor sprite
    elif event == "-ARMOR-":

        # Update the main image with the sprite the user has selected... again... and one last time
        window["-IMAGE-"].update("armor/" + values["-ARMOR-"][0] + ".png")

    # Check if the user has typed something in the character search box
    elif event == "-SEARCH-CHARS-":

        # Update the character sprite list with sorted images
        window["-CHARS-"].update(search(listdir("chars"), values["-SEARCH-CHARS-"]))

    # Check if the user has typed something in the pants search box
    elif event == "-SEARCH-PANTS-":

        # Update the pants sprite list with the sorted items
        window["-PANTS-"].update(search(listdir("pants"), values["-SEARCH-PANTS-"]))

    # Check if the user has typed something in the armor search box
    elif event == "-SEARCH-ARMOR-":

        # Update the armor sprite list with the sorted items
        window["-ARMOR-"].update(search(listdir("armor"), values["-SEARCH-ARMOR-"]))

# You must like reading code, have a cookie 🍪