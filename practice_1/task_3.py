"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""


def CalculateBMI(weight: float, height: float) -> float:
    return weight/height**2

if __name__ == "__main__":
    weight: str = input()
    height: str = input()

    print(f'Your BMI is: {CalculateBMI(float(weight), float(height))}')