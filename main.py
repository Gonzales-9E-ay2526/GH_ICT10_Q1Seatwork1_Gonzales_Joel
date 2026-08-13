# String Formatting
from pyscript import display, document 


studentname = 'Joel Gabriel Gonzales'
age = 15
height1 = 166

display(f'Hello! My name is <i>{studentname}</i>. I am {age} years old. My height is {height1}cm.', target='result')
document.getElementById('result').innerHTML = f'Hello! My name is <i>{studentname}</i>. I am {age} years old. My height is {height1}cm.'

countries_to_visit = ['America', 'Iceland','China']

student_type = False

student_info = {
    'color': 'pink', 
    'car_brand': 'Suzuki',
    'shoe_size': 9.5,
    'best_friend': 'Franco'
}

favorite_fruits = {'Lansones', 'Tangerines', 'Watermelon', 'Banana', 'Grape'}

days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

display(f"Countries to Visit: {countries_to_visit}", target='result')
display(f"Is New Student: {student_type}", target='result')
display(f"User Details: {student_info}", target='result')
display(f"Favorite Fruits: {favorite_fruits}", target='result')
display(f"Days of the Week: {days_of_week}", target='result')