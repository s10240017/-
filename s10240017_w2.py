# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#1
import math
r = float(input("請輸入員的半徑:"))
周長 =2 * math.pi * r
面積 =math.pi * (r**2) 
print(f"半徑為{r}，周長為:{周長:.2f}, 面積為:{面積:.2f}")

#2
name = input("請輸入你的姓名:")
age = int(input("請輸入你的年齡:"))
height = float(input("請輸入你的身高(米):"))
favorite_color = input("請輸入你喜歡的顏色:")


user_data = {
    "姓名": name,
    "年齡": age,
    "身高": height,
    "喜歡的顏色": favorite_color,
}

summary = f"{user_data['姓名']},{user_data['年齡']}歲,{user_data['身高']}米,{user_data['喜歡的顏色']}"

print(summary)

#3
while True:
    try:
        user_input = input("請輸入一個整數:")
        number = int(user_input)
        if number % 2 ==0:
            print(f"{number}是偶數。")
        else:
            print(f"{number}是奇數。")
        break
    
    except ValueError:
        print("錯誤:請輸入一個有效整數。")

 














