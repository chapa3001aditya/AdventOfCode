with open(r'2023/Day 4/input.txt','r') as text:
    text = text.readlines()
    text = list(map(lambda x : x.strip().split('|'),text))

points = list()
gift_cards = [1 for i in range(len(text))]
for card in text:
    card[0] = card[0].split(':')
    card[0] = [int(x) for x in card[0][1].strip().split(" ") if x.isdigit()]
    card[1] = [int(x) for x in card[1].strip().split(" ") if x.isdigit()]
    result = [i for i in card[1] if i in card[0]]
    i = text.index(card)
    for j in range(len(result)):
        gift_cards[j+i+1] = gift_cards[i] + gift_cards[j+i+1]

print(sum(gift_cards))
