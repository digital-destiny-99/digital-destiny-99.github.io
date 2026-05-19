# main.py
# Ozzy and The Tall Man
# A Python text adventure about Jesse searching the neighborhood for his dog, Ozzy.
# I rebuilt this as a cleaner portfolio version of a class style final project.

import time


# -----------------------------
# GAME DATA
# -----------------------------

# I used a dictionary for the rooms because each place needs a name, description,
# exits and an item. This keeps the map organized without making the code too advanced.
rooms = {
    "backyard": {
        "name": "Backyard",
        "description": (
            "Jesse stands in the backyard. Ozzy's leash is still hanging from the fence.\n"
            "The gate is open. Deep footprints press into the mud and lead away."
        ),
        "connections": {"north": "alley", "east": "corner_store"},
        "item": "muddy leash",
    },
    "alley": {
        "name": "Alley",
        "description": (
            "The alley is narrow and colder than it should be. A bike is tipped over\n"
            "beside the trash cans. A crumpled note is stuck near the drain."
        ),
        "connections": {"south": "backyard", "east": "empty_lot"},
        "item": "crumpled note",
    },
    "corner_store": {
        "name": "Corner Store",
        "description": (
            "The corner store lights flicker through dusty glass. No one is behind\n"
            "the counter. A flashlight sits by the register, still switched on."
        ),
        "connections": {"west": "backyard", "north": "empty_lot"},
        "item": "flashlight",
    },
    "empty_lot": {
        "name": "Empty Lot",
        "description": (
            "Weeds push through cracked pavement. A strange symbol is scratched\n"
            "into the concrete. A rusted key is half buried near the fence."
        ),
        "connections": {"west": "alley", "south": "corner_store", "north": "old_shed"},
        "item": "rusted key",
    },
    "old_shed": {
        "name": "Old Shed",
        "description": (
            "The shed door hangs crooked. Old tools line the walls and cast thin\n"
            "shadows across the floor. Ozzy's collar sits on the workbench."
        ),
        "connections": {"south": "empty_lot", "east": "playground"},
        "item": "dog collar",
    },
    "playground": {
        "name": "Playground",
        "description": (
            "The swings move even though the air is still. A streetlight buzzes above\n"
            "the slide. A hand drawn map is folded on the bench."
        ),
        "connections": {"west": "old_shed", "north": "haunted_tree_house"},
        "item": "hand drawn map",
    },
    "haunted_tree_house": {
        "name": "Haunted Tree House",
        "description": (
            "The tree house leans over the edge of the neighborhood. A rope ladder\n"
            "hangs from the dark boards. Jesse hears Ozzy whining above him."
        ),
        "connections": {"south": "playground"},
        "item": None,
    },
}


# Jesse needs every item before he can fight the Tall Man and save Ozzy.
required_items = [
    "muddy leash",
    "crumpled note",
    "flashlight",
    "rusted key",
    "dog collar",
    "hand drawn map",
]


# -----------------------------
# DISPLAY FUNCTIONS
# -----------------------------

def separator():
    print("\n" + "*-*" * 20 + "\n")


def pause(seconds=0.25):
    time.sleep(seconds)


def show_title_art():
    separator()
    print("        .-.       .-.       .-.")
    print("       (o o)     (o o)     (o o)")
    print("        |=|       |=|       |=|")
    print("       __|__     __|__     __|__")
    print()
    print("        OZZY AND THE TALL MAN")
    print("        A Python Text Adventure")
    print()
    print("        Find the clues. Face the tree house. Bring Ozzy home.")
    separator()


def show_intro():
    show_title_art()
    pause()
    print("Ozzy is missing.")
    print("Jesse finds the backyard gate open and footprints leading away.")
    print("Somewhere in the neighborhood, the Tall Man is waiting.")


def show_help():
    separator()
    print("COMMANDS")
    print("Move: north, south, east, west")
    print("Move: go north, go south, go east, go west")
    print("Look around: look")
    print("Pick up item: get item")
    print("Check bag: inventory")
    print("See map: map")
    print("Help: help")
    print("Quit: quit")
    separator()


def show_map():
    print("NEIGHBORHOOD MAP")
    print()
    print("              [Haunted Tree House]")
    print("                       |")
    print("                  [Playground]")
    print("                       |")
    print("        [Old Shed] --- |")
    print("             |")
    print("        [Empty Lot]")
    print("          /       \\")
    print("     [Alley]   [Corner Store]")
    print("          \\       /")
    print("          [Backyard]")
    print()
    print("Start: Backyard")
    print("Goal: Haunted Tree House")


def show_inventory(inventory):
    separator()
    if inventory:
        print("INVENTORY")
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")
    separator()


def show_courage(courage):
    print(f"Courage: {courage}/100")


def show_quit():
    separator()
    print("Jesse steps back from the search for now.")
    print("Ozzy is still out there.")
    separator()


# -----------------------------
# ROOM FUNCTIONS
# -----------------------------

def reset_room_items():
    rooms["backyard"]["item"] = "muddy leash"
    rooms["alley"]["item"] = "crumpled note"
    rooms["corner_store"]["item"] = "flashlight"
    rooms["empty_lot"]["item"] = "rusted key"
    rooms["old_shed"]["item"] = "dog collar"
    rooms["playground"]["item"] = "hand drawn map"
    rooms["haunted_tree_house"]["item"] = None


def display_room(current_room):
    room = rooms[current_room]
    separator()
    print(room["name"].upper())
    print(room["description"])
    print()

    if room["item"]:
        print(f"You notice: {room['item']}")
    else:
        print("There is nothing new to pick up here.")

    print()
    print("Exits:", ", ".join(room["connections"].keys()))
    separator()


def pick_up_item(current_room, inventory, courage):
    room = rooms[current_room]
    item = room["item"]

    if item is None:
        print("There is nothing here to pick up.")
        return inventory, courage

    if item in inventory:
        print(f"You already have the {item}.")
        return inventory, courage

    inventory.append(item)
    room["item"] = None
    courage = min(100, courage + 7)

    print(f"You picked up the {item}.")
    print("Jesse feels a little braver.")

    return inventory, courage


def get_direction(command):
    if command.startswith("go "):
        return command.replace("go ", "", 1).strip()
    return command


def move_player(current_room, direction, inventory, courage):
    room = rooms[current_room]

    if direction not in room["connections"]:
        courage = max(0, courage - 4)
        print("Jesse cannot go that way.")
        return current_room, courage

    next_room = room["connections"][direction]

    if next_room == "haunted_tree_house" and not has_all_items(inventory):
        courage = max(0, courage - 10)
        separator()
        print("Jesse reaches the bottom of the tree house ladder.")
        print("The boards creak above him. The Tall Man is close.")
        print("Jesse is not ready yet. He needs every clue before going up.")
        print("The fear pushes him back to the playground.")
        separator()
        return "playground", courage

    return next_room, courage


# -----------------------------
# GAME LOGIC FUNCTIONS
# -----------------------------

def has_all_items(inventory):
    for item in required_items:
        if item not in inventory:
            return False
    return True


def missing_items(inventory):
    missing = []

    for item in required_items:
        if item not in inventory:
            missing.append(item)

    return missing


def check_final_room(current_room, inventory):
    return current_room == "haunted_tree_house" and has_all_items(inventory)


def fight_tall_man():
    separator()
    print("Jesse climbs into the haunted tree house.")
    pause()
    print("The Tall Man unfolds from the shadows, taller than the roof should allow.")
    pause()
    print("Jesse holds up every clue he found.")
    print("The muddy leash. The note. The flashlight. The key. The collar. The map.")
    pause()
    print("The tree house shakes. The Tall Man screams like old wood splitting.")
    pause()
    print("Ozzy bursts from behind a broken crate and runs straight into Jesse's arms.")
    pause()
    print()
    print("YOU WIN")
    print("Jesse saved Ozzy and escaped the Tall Man.")
    separator()


def ask_replay():
    while True:
        answer = input("Play again? yes/no > ").strip().lower()

        if answer in ["yes", "y"]:
            return True

        if answer in ["no", "n"]:
            print("Thanks for playing Ozzy and The Tall Man.")
            return False

        print("Please type yes or no.")


# -----------------------------
# MAIN GAME LOOP
# -----------------------------

def play_game():
    reset_room_items()

    inventory = []
    courage = 60
    current_room = "backyard"

    show_intro()
    show_help()
    display_room(current_room)

    while True:
        show_courage(courage)
        print()
        command = input("What do you do? > ").strip().lower()

        if command == "":
            print("Type a command. Use help if you need the list.")
            continue

        if command == "quit":
            show_quit()
            break

        elif command == "help":
            show_help()

        elif command == "map":
            separator()
            show_map()
            separator()

        elif command == "look":
            display_room(current_room)

        elif command == "inventory":
            show_inventory(inventory)

        elif command in ["get", "get item", "get items"] or command.startswith("get "):
            inventory, courage = pick_up_item(current_room, inventory, courage)

        elif command in ["north", "south", "east", "west"] or command.startswith("go "):
            direction = get_direction(command)
            current_room, courage = move_player(current_room, direction, inventory, courage)
            display_room(current_room)

            if check_final_room(current_room, inventory):
                fight_tall_man()
                break

        else:
            courage = max(0, courage - 5)
            print(f"\n'{command}' is not a command Jesse understands.")
            print("Try help, map, inventory, get item or go north.")

    if ask_replay():
        play_game()


# -----------------------------
# START GAME
# -----------------------------

if __name__ == "__main__":
    play_game()
