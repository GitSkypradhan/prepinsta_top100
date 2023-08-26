# calculate body max index

def bmi_calc(weight_kg:float,height_cm:float) ->None:
    bmi = weight_kg/(height_cm/100)**2
    result(bmi)

def result(bmi):
    print('Under Weight') if bmi < 18.5 else print('Normal Weight') if bmi >= 18.5 and bmi <= 24.9 else print('Overweight') if bmi >=25  and bmi <29.9 else print("Obese")
    print(f"Your BMI is :{bmi:.2f}")


bmi_calc(65,167)
