import random
def play_game():
    with open("words.txt", "r") as input_file:
        contents = input_file.read()
    word = random.choice((contents).split())
    print(word)
    spaces = ['_'] * len(word)

    user_guesses(word, spaces)  

def get_letter_position(guess, word, spaces):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess)
            removed_character ='*'
            word = word[:index]+removed_character+word[index+1:]
            spaces[index] = guess
        else:
            index = -1
    return (word, spaces)
def win_check(spaces):
    for i in range(0, len(spaces)):
        if spaces[i] == '_':
            return -1
    return 1
def user_guesses(word, spaces):
    num_turns = len(word)
    for i in range(0, num_turns + 1):  
        guess = input('Guess a character:')
        if guess in word:
            word, spaces = get_letter_position(guess, word, spaces)
            print(spaces)
        else:
            print('Sorry that letter is not in the word.')
        if win_check(spaces) == 1:
            print('Congratulations you won')
            break
        print('you have '+str(num_turns - i)+' turns left.')
        print()
        if (num_turns - i) == 0:
            print('GAME OVER, you suck')
            break

if __name__ == "__main__":
    play_game()