import random

def main():
    RandomNumber : int =  random.randint(1,100)
    Guessed = False
    print(RandomNumber)
    print('adivina el numero de 1 a 100')
    while Guessed == False:
        GuessNumber = input('Write your guess: ')
        if int(GuessNumber) == RandomNumber:
            Guessed = True
            print("You Win!")
            break
        elif GuessNumber == '--kill' or GuessNumber == '-k':
            break
        else:
            print("Keep trying!")

if __name__ == '__main__':
    main()