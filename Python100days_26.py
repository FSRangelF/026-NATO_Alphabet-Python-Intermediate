import pandas
import random

new_list = [n*2 for n in range(1,5)]
print(new_list)

names = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
new_names = [name.upper() for name in names if len(name)<= 4]
print(new_names)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(item) for item in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)

all_states = ['arizona', 'texas', 'idaho']
guessed_state = ['arizona']
pandas.DataFrame([state for state in all_states if state not in guessed_state]).to_csv('states.csv')


student_scores = {student:[random.randint(0,100) for i in range(5)] for student in names}
passed_students = {student:sum(score)/len(score) for (student, score) in student_scores.items() if sum(score)/len(score) > 50 }
print(student_scores)
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp*9/5)+32 for (day, temp) in weather_c.items()}
print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
for (key, value) in student_dict.items():
    print(key, value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop trhough columns
for (key, value) in student_data_frame.items():
    print(value)

# in-built loop trhough rows
for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.student, row.score)