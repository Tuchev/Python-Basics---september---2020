price_for_one_page = float(input())
price_for_one_cover = float(input())
discount_for_paper_percent = int(input())
sum = float(input())
percent_of_team = int(input())

price_for_all_pages = price_for_one_page * 899
price_for_all_covers = price_for_one_cover * 2

total_price_of_book = price_for_all_covers + price_for_all_pages

book_after_discount = total_price_of_book - (total_price_of_book * discount_for_paper_percent / 100)

total_sum_for_designer = book_after_discount + sum

total_sum = total_sum_for_designer - (total_sum_for_designer * percent_of_team / 100)

print(f"Avtonom should pay {total_sum:.2f} BGN.")

