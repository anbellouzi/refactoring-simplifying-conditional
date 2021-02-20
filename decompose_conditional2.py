
# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120

def is_good_level_cholestrol():
    return (total_cholostrol < 200 and ldl < 100 and triglyceride < 150)

def is_high_level_cholestrol():
    return (200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200)

def is_moderate_level_cholestrol():
    return (200 <total_cholostrol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200)
    
    
if is_good_level_cholestrol():
    # good level
    print('*** Good level of cholestrol ***')
elif is_high_level_cholestrol():
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
elif is_moderate_level_cholestrol():
    #TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
else:
    print('Error: unhandled case.')