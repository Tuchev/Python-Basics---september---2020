num_of_peoples = int(input())
num_of_overnights = int(input())
num_of_card_for_transport = int(input())
num_of_tickets_for_museum = int(input())

sum_of_overnights = num_of_overnights * 20
sum_of_card_for_transport = num_of_card_for_transport * 1.60
sum_of_tickets_for_museum = num_of_tickets_for_museum * 6

total_sum_for_one_person = sum_of_overnights + sum_of_card_for_transport + sum_of_tickets_for_museum
total_sum_for_all = total_sum_for_one_person * num_of_peoples
total_sum_for_all_after_percentage = total_sum_for_all * 1.25
print(f"{total_sum_for_all_after_percentage:.2f}")