### ekids2024
Ekids program 2024 Python 1

Це проект сторена в навчальних цілях для демонстарції роботи з GitHub

```
#height = float(input("Height-"))
height = 1.76
#weight = float(input("Weight-"))
weight = 80

bmi = weight / (height ** 2)
print (str(bmi))
#print (str(int(bmi)))
print ("Your body mass index is " + str(round(bmi,1)))

if bmi < 18.5:
   print("Underweight")
elif bmi >= 18.5 and bmi < 25.5:
    print("Normal")
else:
    print ("Owerweight")






```
