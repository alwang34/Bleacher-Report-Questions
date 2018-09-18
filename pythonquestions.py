import random

'''
Write a number guessing game. Keep asking the user to guess a number between 1 and 100 until they guess correctly.
If the number the user guesses is too high, tell them so. Same with if the number is too low.
Congratulate them when they’ve guessed the correct number and tell them how many guesses they used to get to the correct number.
'''
def guessing_game():
    count = 0
    guess = False
    random_number = random.randint(0,100)

    while guess == False:
        guessed_number = int(input("Enter a guess: "))
        count += 1
        if guessed_number > random_number:
            print("You guessed too high")
        elif guessed_number < random_number:
            print("You guessed too low")
        else:
            print("Congratulations! You guessed correctly")
            guess = True

    print ("Number of guesses: " + str(count))

'''
Write a function that takes in two lists of words and returns a list of the words common to both original lists.
For example, given ["hello", "adios", "goodbye", "hola", "au revoir", "bonjour"] and 
["hello", "welcome","thanks", "goodbye", "please"], 
return ["hello", "goodbye"].
'''
def common_words(list1, list2):
    return list(set(list1).intersection(list2))

'''
Write a function that takes in 3 integers as arguments and returns a list of numbers from 1 to 100 (inclusive), 
containing only integers that are evenly divisible by at least one of the integers.
For example, given 50, 30, and 29, return [29, 30, 50, 58, 60, 87, 90, 100].
'''
def divisibility(number1, number2, number3):
    answer = []
    numbers = [number1, number2, number3]
    for i in range(1,101):
        for j in numbers:
            if i % j == 0:
                answer.append(i)
                break

    return answer


guessing_game()

words = common_words(["hello", "adios", "goodbye", "hola", "au revoir", "bonjour"], ["hello", "welcome","thanks", "goodbye", "please"])
print(words)

numbers = divisibility(50, 30, 29)
print(numbers)
