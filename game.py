from random import randint
sum = 0
playerInput = 0
myInput = 0
while sum <= 100:
    sum += myInput
    print(f"┌──────┬──────────────┬────────┐\n│Player│  Total       │ PC     │\n├──────┼──────────────┼────────┤\n│      │     {sum}", " " * (7 - len(str(sum))), f"│   +{myInput}", " " * (2 - len(str(myInput))), f"│\n└──────┴──────────────┴────────┘")
    if (sum >= 100):
        print("PC WIN")
        break
    playerInput = int(input("Player input:"))
    sum += playerInput
    print(f"┌──────┬──────────────┬────────┐\n│Player│  Total       │ PC     │\n├──────┼──────────────┼────────┤\n│ +{playerInput}", " " * (2 - len(str(playerInput))),f"│     {sum}", " " * (7 - len(str(sum))), f"│        │\n└──────┴──────────────┴────────┘")
    if playerInput > 10 or playerInput < 1:
        print ("Don't break the rules")
        break
    if (sum >= 100):
        print("PLAYER WIN")
        break
    myInput = randint(1, 10)
    print("PC input: ", myInput)
