#!/usr/bin/env python
# coding: utf-8

# In[9]:


weight = int(input("Enter your weight in pounds: "))

print('Enter your height:')

height_in_feets,height_in_inches  = int(input("Foots: ")), int(input("Inches: "))

height = height_in_feets*12 + height_in_inches

BMI = (weight * 703) / (height * height)

print("Your BMI: {:.1f}".format(BMI))

if BMI > 0: 
    if BMI < 18.5:
        print('You are underweight')
    elif BMI >= 18.5 and BMI <= 24.9:
        print('You are normal weight')
    elif BMI >= 25 and BMI <= 29.9:
        print('You are overweight')
    elif BMI >= 30 and BMI <= 34.9:
        print('You are obese')
    elif BMI >= 35 and BMI <= 39.9:
        print('You are severely obese')
    else:
        print('you are morbidly obese')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




