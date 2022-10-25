# Problem

2 players want to play the substring game.

## Rules:

- Both people are given the same string.
- Both people have to make substrings from the string.
- Player 1 has to make substrings starting with consonants.
- Player 2 has to make substrings starting with vowels.
- Game ends when both players have made all possible substrings.

## Scoring:

- A player gets +1 point for each occurrence of the substing in the string.

## Example:
- String S = BANANA
- Player 1's first substring is 'B'
- The substring 'B' occures 1 time. Player 1 will get 1 point.

## Constraints:
- 0 < len(s) <= 10^6

## Input Format:
- A single line of input containing the string.
- The string will only contain uppercase letters [A-Z]

## Output Format:
- Print one line: The name of the player and their score, seperated by a space.
- If the game is a Draw print 'Draw'
