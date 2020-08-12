import random
print("H A N G M A N")
words = ["kotlin", "java", "python", "javascript"]
word_to_guess = random.choice(words)
word_set = set(word_to_guess)
word_to_list = list("-" * len(word_to_guess))
word_set_repeated = set()
lives = 8
ASCII = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"}

while True:
    answer = input('Type "play" to play the game, "exit" to quit:')
    if answer == "exit":
        break
    if answer != "play":
        pass
    else:
        while lives != 0:
            print("\n" + "".join(word_to_list))
            answer = input("Input a letter: ")
            if len(answer) > 1 or len(answer) == 0:
                print("You should input a single letter")
                continue
            if answer not in ASCII:
                print("It is not an ASCII lowercase letter")
                continue
            if answer in word_set_repeated:
                print("You already typed this letter")
                continue
            word_set_repeated.add(answer)
            if answer in word_set:
                if word_to_guess.count(answer) == len(word_to_guess):
                    word_to_list[:] = answer * len(word_to_guess)
                elif word_to_guess.count(answer) == 1:
                    index = word_to_guess.index(answer)
                    word_to_list[index] = answer
                else:
                    indexes = set()
                    index = 0
                    for _ in range(word_to_guess.count(answer)):
                        index = word_to_guess.index(answer, index)
                        indexes.add(index)
                        index += 1

                    for index in indexes:
                        word_to_list[index] = answer
            else:
                lives -= 1
                print("No such letter in the word")
                if lives == 0:
                    print("You are hanged!")
                    break

            if "".join(word_to_list) == word_to_guess:
                print("\n" + "".join(word_to_list))
                print("You guessed the word!\n"
                      "You survived!\n")
                break
