# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:22:07 2024

@author: student
"""

#1
def print_pattern(rows):
    for i in range(1, rows + 1):
       
        print(" " * (rows - i), end="")
        
        for j in range(1, i + 1):
            print(j, end="")
        
        for k in range(i - 1, 0, -1):
            print(k, end="")
        print()

print_pattern(10)  

#2

import math
for i in range(2,100):
    j = 2
    prime = True
    while j <= math.sqrt(i):
        if (i%j == 0):
            prime = False
            break
        j += 1
    if prime:
        print(i,'為質數')
        
#3

def check_invoice(prizes, invoice_number):

    invoice_str = str(invoice_number)
    
    if invoice_str == prizes["特別獎"]:
        return "中了特別獎，獎金 1,000 萬元！"
    
    if invoice_str == prizes["特獎"]:
        return "中了特獎，獎金 200 萬元！"
    
    for head_prize in prizes["頭獎"]:
        if invoice_str == head_prize:
            return "中了頭獎，獎金 20 萬元！"
    
    for i in range(2, 7):
        prize_level = f"{i}獎"
        if prize_level in prizes: 
            for head_prize in prizes["頭獎"]:
                if invoice_str[-i:] == head_prize[-i:]:
                    return f"中了{prize_level}，各得獎金 {prizes[prize_level]} 元！"
    
    return "發票號碼未中獎。"

prizes = {
    "特別獎": "63603594",
    "特獎": "73155944",
    "頭獎": ["94985899", "57283420", "62825278"],
    "二獎": "4萬元",
    "三獎": "1萬元",
    "四獎": "4千元",
    "五獎": "1千元",
    "六獎": "2百元"
}


invoice_number = int(input("請輸入發票號碼："))


result = check_invoice(prizes, invoice_number)
print(result)
        
        
        