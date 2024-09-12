"""
Разработайте программу, запрашивающую у  пользователя целое четырехзначное число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число 3141,
 программа должна вывести 
следующий результат: 3 + 1 + 4 + 1 = 9

@author: Savant
"""

def SumNumbers(number: str) -> int:
    return sum([int(x) for x in number])

if __name__ == "__main__":
    number: str = input()  
    print(SumNumbers(number))