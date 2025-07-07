'''  
@author: 22000409 Kaushal Ramoliya  
@description: 32. - Write a program for next word prediction using N-Gram conditional probability. 
'''
file = open("Program_32_data_file.txt", "r", encoding="utf-8")
text = file.read()
file.close()

print("This is the text data from file:")
#print(text)
print("\n")

words = text.split()
print("This is the list of words:")
#print(words)

di = {}

for i in range(len(words) - 2):
    key = words[i] + " " + words[i+1]
    value = words[i+2]

    if key not in di:
        di[key] = {}

    if value in di[key]:
        di[key][value] += 1
    else:
        di[key][value] = 1

for key, value_dict in di.items():
    total_count = sum(value_dict.values())  
    for value in value_dict:
        value_dict[value] = round(value_dict[value] / total_count, 2)  

print("\nThis is the dictionary with probabilities:")
print(di)

while True:
    user_input = input("Enter a phrase: ")

    if user_input.lower() == "exit":
        break

    print(di.get(user_input, "No matching phrase found"))
