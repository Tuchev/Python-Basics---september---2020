# 1.	Плод - текст с възможности: "Watermelon", "Mango", "Pineapple" или "Raspberry"
# 2.	Размерът на сета - текст с възможности: "small" или "big"
# 3.	Брой на поръчаните сетове - цяло число в интервала [1 … 10000]

#             	    Диня 	        Манго	        Ананас	        Малина
# 2 броя (small)	56 лв./бр.	    36.66 лв./бр.	42.10 лв./бр.	20 лв./бр.
# 5 броя (big)	    28.70 лв./бр.	19.60 лв./бр.	24.80 лв./бр.	15.20 лв./бр.

fruit = input()
size_of_set = input()
number_of_sets = int(input())

price_watermelon_small = number_of_sets * 2 * 56
price_watermelon_big = number_of_sets * 5 * 28.70
price_mango_small = number_of_sets * 2 * 36.66
price_mango_big = number_of_sets * 5 * 19.60
price_pineapple_small = number_of_sets * 2 * 42.10
price_pineapple_big = number_of_sets * 5 * 24.80
price_raspberry_small = number_of_sets * 2 * 20
price_raspberry_big = number_of_sets * 5 * 15.20

if fruit == 'Watermelon' and size_of_set == 'small' and price_watermelon_small < 400:
    print(f'{price_watermelon_small:.2f} lv.')
elif fruit == 'Watermelon' and size_of_set == 'small' and 400 <= price_watermelon_small <= 1000:
    print(f'{(price_watermelon_small * 0.85):.2f} lv.')
elif fruit == 'Watermelon' and size_of_set == 'small' and price_watermelon_small > 1000:
    print(f'{(price_watermelon_small * 0.50):.2f} lv.')
elif fruit == 'Watermelon' and size_of_set == 'big' and price_watermelon_big < 400:
    print(f'{price_watermelon_big:.2f} lv.')
elif fruit == 'Watermelon' and size_of_set == 'big' and 400 <= price_watermelon_big <= 1000:
    print(f'{(price_watermelon_big * 0.85):.2f} lv.')
elif fruit == 'Watermelon' and size_of_set == 'big' and price_watermelon_big > 1000:
    print(f'{(price_watermelon_big * 0.50):.2f} lv.')

elif fruit == 'Mango' and size_of_set == 'small' and price_mango_small < 400:
    print(f'{price_mango_small:.2f} lv.')
elif fruit == 'Mango' and size_of_set == 'small' and 400 <= price_mango_small <= 1000:
    print(f'{(price_mango_small * 0.85):.2f} lv.')
elif fruit == 'Mango' and size_of_set == 'small' and price_mango_small > 1000:
    print(f'{(price_mango_small * 0.50):.2f} lv.')
elif fruit == 'Mango' and size_of_set == 'big' and price_mango_big < 400:
    print(f'{price_mango_big:.2f} lv.')
elif fruit == 'Mango' and size_of_set == 'big' and 400 <= price_mango_big <= 1000:
    print(f'{(price_mango_big * 0.85):.2f} lv.')
elif fruit == 'Mango' and size_of_set == 'big' and price_mango_big > 1000:
    print(f'{(price_mango_big * 0.50):.2f} lv.')

elif fruit == 'Pineapple' and size_of_set == 'small' and price_pineapple_small < 400:
    print(f'{price_pineapple_small:.2f} lv.')
elif fruit == 'Pineapple' and size_of_set == 'small' and 400 <= price_pineapple_small <= 1000:
    print(f'{(price_pineapple_small * 0.85):.2f} lv.')
elif fruit == 'Pineapple' and size_of_set == 'small' and price_pineapple_small > 1000:
    print(f'{(price_pineapple_small * 0.50):.2f} lv.')
elif fruit == 'Pineapple' and size_of_set == 'big' and price_pineapple_big < 400:
    print(f'{price_pineapple_big:.2f} lv.')
elif fruit == 'Pineapple' and size_of_set == 'big' and 400 <= price_pineapple_big <= 1000:
    print(f'{(price_pineapple_big * 0.85):.2f} lv.')
elif fruit == 'Pineapple' and size_of_set == 'big' and price_pineapple_big > 1000:
    print(f'{(price_pineapple_big * 0.50):.2f} lv.')

elif fruit == 'Raspberry' and size_of_set == 'small' and price_raspberry_small < 400:
    print(f'{price_raspberry_small:.2f} lv.')
elif fruit == 'Raspberry' and size_of_set == 'small' and 400 <= price_raspberry_small <= 1000:
    print(f'{(price_raspberry_small * 0.85):.2f} lv.')
elif fruit == 'Raspberry' and size_of_set == 'small' and price_raspberry_small > 1000:
    print(f'{(price_raspberry_small * 0.50):.2f} lv.')
elif fruit == 'Raspberry' and size_of_set == 'big' and price_raspberry_big < 400:
    print(f'{price_raspberry_big:.2f} lv.')
elif fruit == 'Raspberry' and size_of_set == 'big' and 400 <= price_raspberry_big <= 1000:
    print(f'{(price_raspberry_big * 0.85):.2f} lv.')
elif fruit == 'Raspberry' and size_of_set == 'big' and price_raspberry_big > 1000:
    print(f'{(price_raspberry_big * 0.50):.2f} lv.')