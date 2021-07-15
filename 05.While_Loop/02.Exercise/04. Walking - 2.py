target_steps = 10000
total_steps = 0
command = input()

while command != "Going home":
    current_steps = int(command)
    total_steps += current_steps
    if total_steps >= target_steps:
        break
    command = input()


if command == "Going home":
    command = input()
    total_steps += int(command)
diff = abs(target_steps - total_steps)
if total_steps >= target_steps:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")