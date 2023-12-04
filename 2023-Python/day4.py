#!/usr/bin/python3

infile = open("input/day4_input.txt","r")
card_winnings = []
card_deck = []
current_card = 1

def card_round():
    global card_deck
    new_deck = []
    winnings = 0

    for card in card_deck:
        for card_increment in range(card_winnings[card-1]):
            winnings += card_winnings[card-1]
            new_deck.append(card + card_increment + 1)
    card_deck = new_deck

    return winnings

for l in infile:
    line = l.strip()
    card_numbers = line.split(": ")[1].split(" | ")
    my_numbers = card_numbers[0].split()
    winning_numbers = card_numbers[1].split()
    card_deck.append(current_card)

    matching = 0
    for m in my_numbers:
        for w in winning_numbers:
            if m == w:
                matching += 1

    card_winnings.append(matching)
    current_card += 1

infile.close()

winning_sum = 0
for s in card_winnings:
    score = 2**(s-1) if s > 0 else 0
    winning_sum += score

print("Part 1: ", winning_sum)

total_cards = 0
round_winnings = 1

while round_winnings > 0:
    total_cards += len(card_deck)
    round_winnings = card_round()

print("Part 2: ", total_cards)