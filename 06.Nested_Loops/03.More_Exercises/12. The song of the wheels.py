control_num = int(input())
password_count = 0
password = ""
is_Found = False
all_passwords=""
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    if (a * b + c * d) == control_num:
                        password_count += 1
                        if password_count==1:
                            all_passwords += f"{a}{b}{c}{d}"
                        else:
                            all_passwords +=f" {a}{b}{c}{d}"
                        if password_count == 4:
                            password = f"{a}{b}{c}{d}"
                            is_Found = True
print(all_passwords)
if is_Found:
    print(f"Password: {password}")
else:
    print("No!")