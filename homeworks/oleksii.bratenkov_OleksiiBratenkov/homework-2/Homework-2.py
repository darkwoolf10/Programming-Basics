
print ("Hello! Can I ask you a few questions?")
name = input("What is your name? ")
city = input ("Where are you live? ")
age = int(input("What is your age? "))

dict_a = {
    "name": name,
    "city":city,
    "age": age
}
print (dict_a["name"])
print (dict_a)
answer = ("Hello, %s from %s, why you only %i ?" %(name, city, age))
print(answer)
print ("Goodbye" + ", " + dict_a["name"] + " from " + dict_a["city"] + "!" )


file = open ("answers.txt", "w")
file.write(answer)
file.close()
