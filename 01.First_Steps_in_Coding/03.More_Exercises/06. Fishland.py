price_of_skumriq = float(input())
price_of_caca = float(input())
palamud_in_kg = float(input())
safrid_in_kg = float(input())
midi_in_kg = int(input())

total_sum_of_palamud = (price_of_skumriq + (price_of_skumriq * 0.60)) * palamud_in_kg
total_sum_of_safrid = (price_of_caca + (price_of_caca * 0.80)) * safrid_in_kg
total_sum_of_midi = midi_in_kg * 7.50

total_sum = total_sum_of_palamud + total_sum_of_safrid + total_sum_of_midi
print(f'{total_sum: .2f}')