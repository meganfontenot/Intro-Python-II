import random
import textwrap
from room import Room
from player import Player

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance", "North of you, the cave mouth beckons", tool="compass"
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        tool="flash-light",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        tool="climbing-rope",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        tool="Empty Canten of water",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        tool="Empty Treasure Chest",
    ),
}


# Link rooms together
room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# #
# Main
#


def intro():
    print(
        """
        You are the fiercely independent grandchild of an eccentric adventurer who vanished years earlier. Hoping to solve the mystery of your grandfather's disappearance, you must embark on a perilous journey to his last-known destination -- a fabled tomb on a mythical island that might be somewhere off the coast of Japan. The stakes couldn't be higher as you must rely on your sharp mind, blind faith and stubborn spirit to venture into the unknown.
        """
    )


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
intro()

Player1 = Player(
    name=input("Please choose Player Name: "),
    description=input("Enter Player Strengths: "),
    fanny_pac=" no items",
    current=room["outside"],
)

playerDescription = []

for player in range(1):
    playerDescription.append(Player1.name.strip())
    playerDescription.append(Player1.description)
    playerDescription.append(Player1.fanny_pac)
    playerDescription.append("Current: " + Player1.current.name)
    playerDescription.append(Player1.current.description)

print(playerDescription)

