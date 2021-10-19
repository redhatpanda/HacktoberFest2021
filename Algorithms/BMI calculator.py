h=float(input('enter height(cm)'))
w=float(input('enter weight(kg)'))
h=h/100
bmi=w/(h*h)
print('BMI is- ',bmi)
if bmi>0:
  if bmi<=16:
    print('Severely Underweight')
  elif bmi<=18.5:
    print('Underweight')
  elif bmi<=25:
    print('Healthy')
  elif bmi<=30:
    print('Overweight')
  else:
    print('Severly Overweight')
else:
  print('invalid details')
