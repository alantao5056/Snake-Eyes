from random import randint


s = "+ - - - - +"
m1 = "|  o   o  |"
m2 = "|  o      |"
m3 = "|    o    |"
m4 = "|      o  |"
m5 = "|         |"

dice = [
  [m5, m3, m5],
  [m2, m5, m4],
  [m2, m3, m4],
  [m1, m5, m1],
  [m1, m3, m1],
  [m1, m1, m1]
]


def die(i):
  return [s, *dice[i - 1], s]


def join_row(*rows):
  return ['   '.join(r) for r in zip(*rows)]


def twoDice(a, b):
  for line in join_row(die(a), die(b)):
    print(line)


def enterNumOfRounds():
  while True:
    try:
      rounds = int(input("Please enter the number of rounds: "))
      return rounds
    except ValueError:
      print("invalid input")


def askIfReady():
  while True:
    ready = input("ARE YOU READY??? (y/n): ")
    if ready == "y" or ready == "yes":
      return True
    else:
      return False


def askIfKeepRolling():
  while True:
    rolling = input("Keep rolling? (y/n): ")
    if rolling == "y" or rolling == "yes":
      return True
    elif rolling == "n" or rolling == "no":
      return False


def askIfContinue():
  while True:
    yes = input("press enter to continue...\n\n\n")
    if yes == "":
      break


def startGame(rounds: int):
  for i in range(1, rounds + 1):
    print(f"ROUND {i}:")
    roundTotal = 0
    firstRound = True
    while True:
      a, b = randint(1, 6), randint(1, 6)
      total = a + b
      twoDice(a, b)
      print(f"you rolled {a}, {b}. Together is {total}")
      if a == b:
        if firstRound:
          print("Not over yet! Roll again.")
        else:
          if a == 1:
            print("SNAKE EYES! NO POINTS FOR YOU!\n\n")
          else:
            print("A double! ROUND OVER.\n\n")
          askIfContinue()
          break
      else:
        roundTotal += total
        print(f"The current number of points is {roundTotal}\n\n")
      if not askIfKeepRolling():
        break
      firstRound = False
  printEndLine()


def printBanner():
  print("##########################################################################\n")
  print("           _____ _   _   ___   _   __ _____   _______   _______ _____")
  print("          /  ___| \ | | / _ \ | | / /|  ___| |  ___\ \ / /  ___/  ___|")
  print("          \ `--.|  \| |/ /_\ \| |/ / | |__   | |__  \ V /| |__ \ `--. ")
  print("           `--. \ . ` ||  _  ||    \ |  __|  |  __|  \ / |  __| `--. \ ")
  print("          /\__/ / |\  || | | || |\  \| |___  | |___  | | | |___/\__/ /")
  print("          \____/\_| \_/\_| |_/\_| \_/\____/  \____/  \_/ \____/\____/ \n")
  print("Copyright 2020 Snake Eyes by Alan Tao\n")
  print("##########################################################################\n")
  return 0


def printEndLine():
  print("  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______       __  ")
  print(" /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     |  | ")
  print("|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    |  | ")
  print("|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     |  |")
  print("|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.|__| ")
  print(" \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|(__) \n\n\n")

  print("Thanks for playing Snake Eyes!!!")


def main():
  printBanner()
  rounds = enterNumOfRounds()
  if askIfReady():
    startGame(rounds)
  return 0


main()
