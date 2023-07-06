import random

def Count_cards(Hand):
    Card_Aomount = 0
    for i in range(len(Hand)):
       Card_Aomount += (Hand[i][0] + Hand[i][1])
    return Card_Aomount

for Boss_Loop in range(5):
    Avg_Cards = 0
    domino_set = ['']*28
    card = []
    count = 0

    for x in range(7):
        for z in range(x, 7):
            card = [x,z]
            domino_set[count] = card
            count += 1


    Hand_list = []
    Card_count = []
    c_amount = 0


    for dice in range(4):
        Hand_list = random.sample(domino_set,7)
        print(Hand_list)
        c_amount = Count_cards(Hand_list)
        Card_count.append(c_amount)
        for loop in range(len(Hand_list)):
            domino_set.remove(Hand_list[loop])

    Avg_Cards = (sum(Card_count)/len(Card_count))
    print(Card_count)
    print(Avg_Cards)
    print('')