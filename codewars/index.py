def between(a, b):
    return list(range(a, b + 1))

def repeat_str(repeat, string):
    return string * repeat

def find_average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) >= 1 else 0

def century(years):
    century = 0
    if years >= 1000 :
        if int(str(years)[-2:]):
            century = int(str(years)[:2]) + 1
        else: century = int(str(years)[:2])
    elif years >= 100 :
        if int(str(years)[-2:]):
            century = int(str(years)[:1]) + 1
        else: century = int(str(years)[:1])
    else : century = 1
    return century

def quarter_of(month):
    if month in range(1,4):
        return 1
    elif month in range(4,6):
        return 2
    elif month in range(7,10):
        return 3
    elif month in range(10,13):
        return 4

def sum_array(a):
    return sum(a)

def bmi(weight, height):
    bmi = weight / pow(height, 2)
    if bmi <= 18.5 :
        return 'Underweight'
    elif bmi <= 25.0 :
        return 'Normal'
    elif bmi <= 30.0 :
        return 'Overweight'
    else: return 'Obese'

print(bmi(208,1.8))
print(bmi(220,1.4))
#Solved python question: Calculate BMI