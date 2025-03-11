# clicat - Your Command Line Virtual Cat
clicat is a virtual cat in your command line. It's a fun little companion that responds to your care through simple cl arguments.

## Features

- Pet status is saved between sessions
- Hunger, happiness, energy, and health change over time
- ASCII art displays your pet's current mood
- Your pet can mimic commands from your bash history (with privacy filters)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/clicat.git
cd clicat

# Make the main file executable
chmod +x main.py
```

## Usage

```bash
# Basic interaction
python main.py

# Feed
python main.py --feed

# Play
python main.py --play

# Let your pet rest
python main.py --rest

# Give medicine
python main.py --heal

# Rename
python main.py --rename Snowball

# Check pet status
python main.py --status
```

## How it Works

Your pet has four main attributes:

- **Hunger**: Decreases over time and when playing. Increases when fed.
- **Happiness**: Decreases over time. Increases when playing.
- **Energy**: Increases over time when resting. Decreases when playing.
- **Health**: Decreases if hunger or happiness is too low. Can be restored with medicine.

## Pet States

- 😊 **Happy**: clicat is doing great!
- 😋 **Hungry**: needs food
- 😴 **Sleepy**: needs rest
- 🤒 **Sick**: needs medicine
- 🎮 **Playing**: Your pet is in a playful mood

## Data Storage

Your pet's state is stored in `~/.clipet` as a JSON file.
