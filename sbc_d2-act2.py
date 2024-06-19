from random import randint
while True:


    p1 = input("FOLD OR UNFOLD : ")
    c2 = randint(0,1)
    c3 = randint(0,1)

    choice = {
        0:"FOLD",
        1:"UNFOLD"
    }

    c2choice = choice[c2]
    c3choice = choice[c3]

    if p1 == "FOLD" and c2choice == "FOLD"  and c3choice == "UNFOLD" or p1 == "UNFOLD" and c2choice == "UNFOLD"  and c3choice == "FOLD":
        print(p1,c2choice,c3choice,"c3 win")
    

    elif p1 == "FOLD" and c2choice == "UNFOLD"  and c3choice == "FOLD" or p1 == "UNFOLD" and c2choice == "FOLD"  and c3choice == "UNFOLD":
        print("PLAYER - 1",p1,"c - 2",c2choice,"c3",c3choice,"c2 win")  
        
       

    elif p1 == "UNFOLD" and c2choice == "FOLD"  and c3choice == "FOLD" or  p1 == "FOLD" and c2choice == "UNFOLD"  and c3choice == "UNFOLD":
        print("PLAYER - 1",p1,"c - 2",c2choice,"c3",c3choice,"P1 win")
 
        
    else:
        print("PLAYER - 1",p1,"c - 2",c2choice,"c3",c3choice,"draw")