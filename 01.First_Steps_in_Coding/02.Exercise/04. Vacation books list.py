#1.	Брой страници в текущата книга – цяло число;
#2.	Страници, които може да прочита за 1 час – цяло число;
#3.	Броя на дните, за които трябва да прочете книгата – цяло число;
number_of_page_in_book = int(input())
page_for_one_hour = int(input())
number_of_day = int(input())
total_time_for_reading = number_of_page_in_book / page_for_one_hour
total_time = total_time_for_reading / number_of_day
print(total_time)