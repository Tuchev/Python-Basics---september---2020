name = input()
password = input()
input_passwoed = input()
while input_passwoed != password:
    input_passwoed = input()
else:
    print(f"Welcome {name}!")