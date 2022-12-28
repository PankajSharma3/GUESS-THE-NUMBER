a=18
c=5
while (True):
    i=int(input("Enter the number:"))
    while (True):
        c=c-1
        print(c,"Chances are left")
        c==0
        break
    if c==0:
        if i==a:
            print("YOU WIN")
        print("Game Over")
        break
    elif i==a:
        print("YOU WIN")
        break
    elif i<a:
        print("INCREASE THE NUMBER")
        continue
    elif i>a:
        print("DECREASE THE NUMBER")
        continue