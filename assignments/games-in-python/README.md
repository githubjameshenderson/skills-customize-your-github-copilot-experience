
# 📘 Assignment: Games in Python

## 🎯 Objective

Practice Python fundamentals by building a classic Hangman game. Students will use variables, strings, loops, conditionals, and user input to create an interactive word-guessing game.

## 📝 Tasks

### 🛠️ Create the Game Setup

#### Description
Build the basic structure for a Hangman game by creating a word list and selecting a random word for each round.

#### Requirements
Completed program should:

- Store a list of words in Python
- Select one word at random from the list
- Display the word as hidden placeholders such as `_ _ _`
- Show the player how many letters are in the word

### 🛠️ Track Player Guesses

#### Description
Allow the player to guess letters and update the game state as they make correct or incorrect guesses.

#### Requirements
Completed program should:

- Prompt the user for a single letter guess using `input()`
- Check whether the guessed letter appears in the secret word
- Reveal matching letters in the hidden word display
- Track incorrect guesses and remaining attempts
- Handle repeated guesses clearly and consistently

### 🛠️ Finish the Game and Show Results

#### Description
Add the end-of-game logic so the player can win or lose based on their guesses.

#### Requirements
Completed program should:

- End the game when the word is fully guessed
- End the game when the player runs out of attempts
- Display a win message when the player succeeds
- Display a lose message when the player fails
- Reveal the full word at the end of the round
- Use clear, friendly text to guide the player through the game
