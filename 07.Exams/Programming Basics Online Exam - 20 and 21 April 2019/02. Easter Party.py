number_of_guests = int(input())
envelope_per_person = float(input())
budget = float(input())

price_of_cake = budget * 0.1

if 10 <= number_of_guests <= 15:
    envelope_per_person *= 0.85
elif 15 < number_of_guests <= 20:
    envelope_per_person *= 0.8
elif number_of_guests > 20:
    envelope_per_person *= .75

total_sum_for_envelope = number_of_guests * envelope_per_person
total_sum = total_sum_for_envelope + price_of_cake
difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")