height = input('請輸入你的身高(CM): ')
weight = input('請輸入你的體重(KG): ')
height = int(height)
weight = int(weight)
bmi = weight / ((height/100) * (height/100))
print(bmi)
if bmi < 18.5:
    print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('正常範圍')
elif bmi >= 24 and bmi < 27:
    print('過重')
elif bmi >= 27 and bmi < 30:
    print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('中度肥胖')
else:
    print('重度肥胖')