def bmi_calculator(weight, height):
    bmi = weight / (height * height)
    if bmi < 18.5:
        category = 'Underweight'
    elif bmi < 25:
        category = 'Normal weight'
    elif bmi < 30:
        category = 'Overweight'
    else:
        category = 'Obese'
    return round(bmi,2), category
