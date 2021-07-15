#1.	Дължина в см – цяло число
#2.	Широчина в см – цяло число
#3.	Височина в см – цяло число
#4.	Процент зает обем – реално число
#V=a.b.c
# Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.
#1 Кубичен дециметър = 1000 Кубичен сантиметър
length = int(input())
width = int(input())
height = int(input())
percentage_is_occupied_by_volume = float(input())
volume = length * width * height
total_volume_in_liters = volume / 1000
total_volume = total_volume_in_liters - (total_volume_in_liters * percentage_is_occupied_by_volume / 100)
print(total_volume)