# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:45:35 2024

@author: student
"""
#1
# 建立字母對應的字典
transform = {}
transform["a"] = "A"
transform["b"] = "B"
transform["c"] = "C"
transform["d"] = "D"
transform["e"] = "E"
transform["f"] = "F"
transform["g"] = "G"
transform["h"] = "H"
transform["i"] = "I"
transform["j"] = "J"
transform["k"] = "K"
transform["l"] = "L"
transform["m"] = "M"
transform["n"] = "N"
transform["o"] = "O"
transform["p"] = "P"
transform["q"] = "Q"
transform["r"] = "R"
transform["s"] = "S"
transform["t"] = "T"
transform["u"] = "U"
transform["v"] = "V"
transform["w"] = "W"
transform["x"] = "X"
transform["y"] = "Y"
transform["z"] = "Z"

input_string = input(":")
input_string = list(input_string)
for i in range(len(input_string)):
    input_string[i] = transform[input_string[i]]
    
output_string = "".join(input_string)
print(":",output_string)


#2
import random

# 使用者輸入
n = int(input("n: "))
a = int(input("a: "))
b = int(input("b: "))

random_choose_list = []

while len(random_choose_list)< n:
    x = random.randint(a, b)
    random_choose_list.append(x)

random_choose_list = set(random_choose_list)
random_choose_list = list(random_choose_list)
random_choose_list.sort()
random_choose_list.reverse()

print(random_choose_list)

#3
import random

# 建立一副撲克牌
suits = ['♠', '♥', '♦', '♣']
ranks = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
deck = [rank + suit for suit in suits for rank in ranks]

# 洗牌
random.shuffle(deck)

# 將牌發給四個人
hands = [[] for _ in range(4)]
for i, card in enumerate(deck):
    hands[i % 4].append(card)

# 將每位玩家手中的牌按照數字大小排序
for hand in hands:
    hand.sort(key=lambda x: ranks.index(x[:-1]))

# 顯示每位玩家手中的牌
for i, hand in enumerate(hands):
    print(f"玩家 {i+1} 的手牌：", hand)





