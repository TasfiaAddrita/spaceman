# Spaceman

## Description
Spaceman is a guessing game. There is a mystery word which the user tries to guess one letter at a time. A placeholder is initially shown, with the number of blanks corresponding to the number of letters in the word. If the letter is in the mystery word, the position(s) of the letter(s) are revealed in the placeholders. Guess the word before you run out of guesses!

## Goals
### Requirements
- [x] User must be able to enter letters to guess
- [x] The user must get accurate feedback on if they guessed a correct letter or an incorrect letter
- [x] The user is always prompted to guess a letter until they win or lose
- [x] The game must use the provided list of words as its source (words.txt).
- [x] User is allowed seven (7) incorrect guesses, and they should be told how many guesses they have left after each incorrect guess
- [x] After guessing a letter, the user must be told the following:
    - [x] Correct guess: the placeholder text with the correct letter filled in.
    - [x] If the word is “dog” and they guess “g” as their first guess, they should see `_ _ g`
- [x] Incorrect guess: a message telling them their guess is incorrect, and then the number of guesses they have remaining
- [x] If a guessed letter appears multiple times in the word, that guessed letter should appear in all valid blanks
- [x] Correct Example (word is “apple”): p → `_ pp_ _`
- [x] Incorrect Example (word is “apple”): p → `_p_ _`
- [x] If a user successfully guesses all the letters, the game ends, and the user is shown a message notifying them that they won
- [x] If a user guesses incorrectly seven (7) times, the game ends, and the user is shown a message notifying them that they lost

### Stretch Challenges
- [x] Alert the user if they guessed a letter they already guessed, and don’t have it count as an incorrect guess
- [x] Users can only guess individual letters at a time. If they guess anything other than an individual letter, they should be prompted and told to input only one letter
- [x] Prompt  the user to play again after a game ends. If they say yes, then start a new game.
- [x] Change the number of incorrect guesses allowed to match the length of the mystery word
- [x] Show the user the mystery word when they lose
- [ ] Use ASCII art to draw the spaceman with each incorrect guess
- [ ] Sinister Spaceman: After the user guesses a correct letter, change the mystery word to be a new mystery word that is the same word length and uses the same correctly guessed letters

## How to run/setup
Instructions on the setup process needed for running locally.

## How to deploy
How to deploy your own instance live.

## Live deployments
Where you can find this project in production

## How to contribute
Fork the current repository and then make the changes that you'd like to said fork. Upon adding features, fixing bugs,
or whatever modifications you've made to the project, issue a pull request to this repository containing the changes that you've made
and I will evaluate them before taking further action. This process may take anywhere from 3-7 days depending on the scope of the changes made,
my schedule, and any other variable factors.

## Resources
External resources used and needed for this project to be completed. Always cite your peer developers!
- [x]
