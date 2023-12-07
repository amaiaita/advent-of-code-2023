# task 1

import re

TEST_INPUT = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''.splitlines()

with open("day7.txt") as f:
    TEST_INPUT = f.read().split("\n")

input = {}
for line in TEST_INPUT:
    hand,bid = line.split(' ')
    input[hand] = bid

hands = list(input.keys())

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []


for hand in hands:
    sorted_hand = ''.join(sorted(hand))
    five = re.compile(r'(.)\1{4}')
    four = re.compile(r'(.)\1{3}')
    three = re.compile(r'(.)\1{2}')
    two = re.compile(r'(.)\1{1}')
    if five.search(sorted_hand):
        five_of_a_kind.append(hand)
    elif four.search(sorted_hand):
        four_of_a_kind.append(hand)
    elif (three.search(sorted_hand)):
        if (len(re.findall(two,re.sub(re.findall(three,sorted_hand)[0],"",sorted_hand)))==1):
            full_house.append(hand)
        else:
            three_of_a_kind.append(hand)
    elif (len(re.findall(two,sorted_hand))==2):
        two_pair.append(hand)
    elif(two.search(sorted_hand)):
        one_pair.append(hand)
    else:
        high_card.append(hand)

values = {
    '2': 'A',
    '3':'B',
    '4':'C',
    '5':'D',
    '6':'E',
    '7':'F',
    '8':'J',
    '9':'K',
    'T':'L',
    'J':'M',
    'Q':'N',
    'K':'O',
    'A':'P'
}

values_swap = {v: k for k, v in values.items()}

def encode_hand(hand):
    encoded_hand=''
    for letter in hand:
        encoded_hand+=values[letter]
    return encoded_hand

def decode_hand(hand):
    decoded_hand = ''
    for letter in hand:
        decoded_hand+=values_swap[letter]
    return decoded_hand

ordered_hands = []

def code_list(list,encode_or_decode):
    coded_list = []
    for item in list:
        coded_list.append(encode_or_decode(item))
    return coded_list

five_of_a_kind = code_list(sorted(code_list(five_of_a_kind,encode_hand)),decode_hand)
four_of_a_kind = code_list(sorted(code_list(four_of_a_kind,encode_hand)),decode_hand)
full_house = code_list(sorted(code_list(full_house,encode_hand)),decode_hand)
three_of_a_kind = code_list(sorted(code_list(three_of_a_kind,encode_hand)),decode_hand)
two_pair = code_list(sorted(code_list(two_pair,encode_hand)),decode_hand)
one_pair = code_list(sorted(code_list(one_pair,encode_hand)),decode_hand)
high_card = code_list(sorted(code_list(high_card,encode_hand)),decode_hand)

cards_in_order = []

cards_in_order.extend(high_card)
cards_in_order.extend(one_pair)
cards_in_order.extend(two_pair)
cards_in_order.extend(three_of_a_kind)
cards_in_order.extend(full_house)
cards_in_order.extend(four_of_a_kind)
cards_in_order.extend(five_of_a_kind)

total_winnings = 0

for i,cards in enumerate(cards_in_order):
    total_winnings+= int(input[cards])*(i+1)

print(total_winnings)