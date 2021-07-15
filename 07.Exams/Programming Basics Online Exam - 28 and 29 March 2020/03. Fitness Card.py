# Пол	Gym	  Boxing	Yoga	Zumba	Dances	Pilates
# мъж	$42	  $41	    $45	    $34	    $51	    $39
# жена	$35	  $37	    $42	    $31	    $53	    $37

#Всички цени на карти за ученици (възраст под 19 години вкл.) са с 20% намаление.

available_amount = float(input())
sex = input()
age = int(input())
sport = input()

total_sum_m_below_19_gym = 42 * 0.80
total_sum_m_below_19_boxing = 41 * 0.80
total_sum_m_below_19_yoga = 45 * 0.80
total_sum_m_below_19_zumba = 34 * 0.80
total_sum_m_below_19_dance = 51 * 0.80
total_sum_m_below_19_pilates = 39 * 0.80

total_sum_f_below_19_gym = 35 * 0.80
total_sum_f_below_19_boxing = 37 * 0.80
total_sum_f_below_19_yoga = 42 * 0.80
total_sum_f_below_19_zumba = 31 * 0.80
total_sum_f_below_19_dance = 53 * 0.80
total_sum_f_below_19_pilates = 37 * 0.80

if sex == 'm' and age <= 19 and sport == 'Gym' and available_amount >= total_sum_m_below_19_gym:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age <= 19 and sport == 'Gym' and available_amount < total_sum_m_below_19_gym:
    print(f"You don't have enough money! You need ${(total_sum_m_below_19_gym - available_amount):.2f} more.")
elif sex == 'm' and age > 19 and sport == 'Gym' and available_amount >= 42:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age > 19 and sport == 'Gym' and available_amount < 42:
    print(f"You don't have enough money! You need ${(42 - available_amount):.2f} more.")

elif sex == 'm' and age <= 19 and sport == 'Boxing' and available_amount >= total_sum_m_below_19_boxing:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age <= 19 and sport == 'Boxing' and available_amount < total_sum_m_below_19_boxing:
    print(f"You don't have enough money! You need ${(total_sum_m_below_19_boxing - available_amount):.2f} more.")
elif sex == 'm' and age > 19 and sport == 'Boxing' and available_amount >= 41:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age > 19 and sport == 'Boxing' and available_amount < 41:
    print(f"You don't have enough money! You need ${(41 - available_amount):.2f} more.")

elif sex == 'm' and age <= 19 and sport == 'Yoga' and available_amount >= total_sum_m_below_19_yoga:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age <= 19 and sport == 'Yoga' and available_amount < total_sum_m_below_19_yoga:
    print(f"You don't have enough money! You need ${(total_sum_m_below_19_yoga - available_amount):.2f} more.")
elif sex == 'm' and age > 19 and sport == 'Yoga' and available_amount >= 45:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age > 19 and sport == 'Yoga' and available_amount < 45:
    print(f"You don't have enough money! You need ${(45 - available_amount):.2f} more.")

elif sex == 'm' and age <= 19 and sport == 'Zumba' and available_amount >= total_sum_m_below_19_zumba:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age <= 19 and sport == 'Zumba' and available_amount < total_sum_m_below_19_zumba:
    print(f"You don't have enough money! You need ${(total_sum_m_below_19_zumba - available_amount):.2f} more.")
elif sex == 'm' and age > 19 and sport == 'Zumba' and available_amount >= 34:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age > 19 and sport == 'Zumba' and available_amount < 34:
    print(f"You don't have enough money! You need ${(34 - available_amount):.2f} more.")

elif sex == 'm' and age <= 19 and sport == 'Dances' and available_amount >= total_sum_m_below_19_dance:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age <= 19 and sport == 'Dances' and available_amount < total_sum_m_below_19_dance:
    print(f"You don't have enough money! You need ${(total_sum_m_below_19_dance - available_amount):.2f} more.")
elif sex == 'm' and age > 19 and sport == 'Dances' and available_amount >= 51:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age > 19 and sport == 'Dances' and available_amount < 51:
    print(f"You don't have enough money! You need ${(51 - available_amount):.2f} more.")

elif sex == 'm' and age <= 19 and sport == 'Pilates' and available_amount >= total_sum_m_below_19_pilates:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age <= 19 and sport == 'Pilates' and available_amount < total_sum_m_below_19_pilates:
    print(f"You don't have enough money! You need ${(total_sum_m_below_19_pilates - available_amount):.2f} more.")
elif sex == 'm' and age > 19 and sport == 'Pilates' and available_amount >= 39:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'm' and age > 19 and sport == 'Pilates' and available_amount < 39:
    print(f"You don't have enough money! You need ${(39 - available_amount):.2f} more.")


elif sex == 'f' and age <= 19 and sport == 'Gym' and available_amount >= total_sum_f_below_19_gym:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age <= 19 and sport == 'Gym' and available_amount < total_sum_f_below_19_gym:
    print(f"You don't have enough money! You need ${(total_sum_f_below_19_gym - available_amount):.2f} more.")
elif sex == 'f' and age > 19 and sport == 'Gym' and available_amount >= 35:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age > 19 and sport == 'Gym' and available_amount < 35:
    print(f"You don't have enough money! You need ${(35 - available_amount):.2f} more.")

elif sex == 'f' and age <= 19 and sport == 'Boxing' and available_amount >= total_sum_f_below_19_boxing:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age <= 19 and sport == 'Boxing' and available_amount < total_sum_f_below_19_boxing:
    print(f"You don't have enough money! You need ${(total_sum_f_below_19_boxing - available_amount):.2f} more.")
elif sex == 'f' and age > 19 and sport == 'Boxing' and available_amount >= 37:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age > 19 and sport == 'Boxing' and available_amount < 37:
    print(f"You don't have enough money! You need ${(37 - available_amount):.2f} more.")

elif sex == 'f' and age <= 19 and sport == 'Yoga' and available_amount >= total_sum_f_below_19_yoga:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age <= 19 and sport == 'Yoga' and available_amount < total_sum_f_below_19_yoga:
    print(f"You don't have enough money! You need ${(total_sum_f_below_19_yoga - available_amount):.2f} more.")
elif sex == 'f' and age > 19 and sport == 'Yoga' and available_amount >= 42:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age > 19 and sport == 'Yoga' and available_amount < 42:
    print(f"You don't have enough money! You need ${(42 - available_amount):.2f} more.")

elif sex == 'f' and age <= 19 and sport == 'Zumba' and available_amount >= total_sum_f_below_19_zumba:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age <= 19 and sport == 'Zumba' and available_amount < total_sum_f_below_19_zumba:
    print(f"You don't have enough money! You need ${(total_sum_f_below_19_zumba - available_amount):.2f} more.")
elif sex == 'f' and age > 19 and sport == 'Zumba' and available_amount >= 31:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age > 19 and sport == 'Zumba' and available_amount < 31:
    print(f"You don't have enough money! You need ${(31 - available_amount):.2f} more.")

elif sex == 'f' and age <= 19 and sport == 'Dances' and available_amount >= total_sum_f_below_19_dance:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age <= 19 and sport == 'Dances' and available_amount < total_sum_f_below_19_dance:
    print(f"You don't have enough money! You need ${(total_sum_f_below_19_dance - available_amount):.2f} more.")
elif sex == 'f' and age > 19 and sport == 'Dances' and available_amount >= 53:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age > 19 and sport == 'Dances' and available_amount < 53:
    print(f"You don't have enough money! You need ${(53 - available_amount):.2f} more.")


elif sex == 'f' and age <= 19 and sport == 'Pilates' and available_amount >= total_sum_f_below_19_pilates:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age <= 19 and sport == 'Pilates' and available_amount < total_sum_f_below_19_pilates:
    print(f"You don't have enough money! You need ${(total_sum_f_below_19_pilates - available_amount):.2f} more.")
elif sex == 'f' and age > 19 and sport == 'Pilates' and available_amount >= 37:
    print(f'You purchased a 1 month pass for {sport}.')
elif sex == 'f' and age > 19 and sport == 'Pilates' and available_amount < 37:
    print(f"You don't have enough money! You need ${(37 - available_amount):.2f} more.")