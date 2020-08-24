names = open('names-11.txt')
nameList = []
for person in names:
  person = person.rstrip()
  nameList.append(person)
print(nameList)
