name = "John Smith"
print(name[1]) # o
print(name[5:9]) # Smit
print(name[5:]) # Smith
print(name[0:4]) # John
print(name[:4]) # John

s ="The quick brown fox jumps over the lazy dog"
print(s[:10]) # The quick
print(s[10:]) # brown fox jumps over the lazy dog

filename="gradebook.pdf"
print(filename[filename.find(".")+1:])

names = "Tom, Dick, Harry" .upper() #lower()
names = names.replace(" ", " ")
nameslist = names.split(",")  # split returns a list ["Tom", "Dick", "Harry"]
print(len(nameslist))
print(nameslist)

# print(filename[-3])