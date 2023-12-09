import re

with open("7.sample.txt", "r") as f:
    buffer = f.read()
    hands = list(map(lambda x : [x[0], int(x[1])], [h.split() for h in buffer.split("\n")]))

char_map = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']

def get_strength(hand):
    unique_char_count = len(set(hand.replace('J','')))
    if unique_char_count == 5:
        type_strength = 1
    elif unique_char_count == 4:
        type_strength = 2
    elif unique_char_count == 3:
        if max([hand.count(char) for char in hand.replace('J','')]) + hand.count('J') == 2:
            type_strength = 3
        else:
            type_strength = 4
    elif unique_char_count == 2:
        if max([hand.count(char) for char in hand.replace('J','')]) + hand.count('J') == 3:
            type_strength = 5
        else:
            type_strength = 6
    else:
        type_strength = 7

    return [type_strength] + [char_map.index(c) for c in hand]

hands = sorted(hands, key=lambda hand: get_strength(hand[0]))
print(str(hands).replace('], [','],\n['))
winnings = [hands[i][1] * (i + 1) for i in range(len(hands))]

print(sum(winnings))