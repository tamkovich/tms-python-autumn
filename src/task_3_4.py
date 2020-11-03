string = input("input nechet str ")
print(f"length of string =  {len(string)}")
index =int(len(string)/2)
center_letter = string[index]
print(f" center letter {center_letter}")
print()
if center_letter == string[0] :
    new_string = string[1:-1]
    print(new_string)