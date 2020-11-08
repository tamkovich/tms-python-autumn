string = input("input  str ")
print(f"length of string =  {len(string)}")
index = 0
if int(len(string)%2) == 0:
    index = int(len(string)/2)-1
else:
    index =int(len(string)/2)
center_letter = string[index]
print(f"center letter {center_letter}")
if center_letter == string[0] :
    new_string = string[1:-1]
    print(f"result {new_string}")
