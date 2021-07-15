#•	Торта  – цената ѝ е 20% от наема на залата
#•	Напитки – цената им е 45% по-малко от тази на тортата
#•	Аниматор – цената му е 1/3 от цената за наема на залата
#•	Наем за залата – цяло число - това се чете от конзолата
rent_for_hall = int(input())
cake = rent_for_hall * 20 / 100
drinks = cake - cake * 45 / 100
animator = rent_for_hall * 1 / 3
total_sum = rent_for_hall + cake + drinks + animator
print(total_sum)