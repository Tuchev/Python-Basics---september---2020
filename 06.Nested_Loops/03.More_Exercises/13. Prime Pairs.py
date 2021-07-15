first = int(input())
second = int(input())
diff_1 = int(input())
diff_2 = int(input())

end_first = first + diff_1
end_second = second + diff_2

for ab in range(first, end_first + 1):
    for cd in range(second, end_second + 1):
        if ab % 2 != 0 and ab % 3 != 0 and ab % 5 != 0 and ab % 7 != 0 and cd % 2 != 0 and cd % 3 != 0 and cd % 5 != 0 and cd % 7 != 0:
            print(f"{ab}{cd}")