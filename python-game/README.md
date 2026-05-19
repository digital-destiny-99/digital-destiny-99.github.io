# Ozzy and The Tall Man

Ozzy and The Tall Man is a Python text adventure about Jesse searching the neighborhood for his missing dog, Ozzy.

The player moves through connected rooms, collects items, checks inventory and follows clues toward the haunted tree house. The game uses simple text commands, a courage meter and conditional logic to decide whether Jesse is ready for the final encounter.

## Portfolio Focus

This project is part of my technical portfolio, but it also connects to UX/UI because the experience depends on clear navigation, readable feedback and simple interaction design.

The player needs to understand:

- where they are
- what they can do next
- what items they have collected
- why the final room is locked behind earlier choices

That makes the project useful as both a beginner Python build and a small study in user flow.

## Features

- Room-based map using Python dictionaries
- Movement commands such as `north`, `south`, `east`, `west` and `go north`
- Inventory system
- Items disappear after pickup
- Help menu with available commands
- ASCII-style map
- Courage meter
- Final room logic that sends the player back if required items are missing
- Win ending after the final Tall Man encounter
- Replay option

## Skills Used

- Python
- Dictionaries
- Lists
- Functions
- Loops
- Conditionals
- Input handling
- Basic game state
- Text-based interface design

## How to Run

You do not need Python installed if you use an online editor.

Open an online Python editor such as Replit, Programiz or OnlineGDB, then copy the code from `main.py` and run it there.

If Python is installed on your computer, download the project folder and run:

```bash
python main.py
```

Depending on your computer, this may also be:

```bash
python3 main.py
```

## Commands

```text
help
map
look
inventory
get item
north
south
east
west
go north
quit
```

## Project Notes

This started as a class-style Python project and was rebuilt into a cleaner portfolio version. I focused on making the code easier to read, organizing the game data more clearly and improving how the player moves through the story.

The project is intentionally simple, but it shows how technical structure can shape an experience.
