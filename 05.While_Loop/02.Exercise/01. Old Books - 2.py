book = input()
input_book = input()
book_counter = 0
while input_book != "No More Books":
    if input_book == book:
        print(f"You checked {book_counter} books and found it.")
        break
    book_counter += 1
    input_book = input()
else:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")