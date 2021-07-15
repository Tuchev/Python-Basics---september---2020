username = input()
pass_for_username = input()
password = input()
while password != pass_for_username:
    password = input()
print(f"Welcome {username}!")