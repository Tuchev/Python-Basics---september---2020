# •	1 биткойн = 1168 лева.
# •	1 китайски юан = 0.15 долара.
# •	1 долар = 1.76 лева.
# •	1 евро = 1.95 лева.
# Обменното бюро има комисионна от 0 до 5 процента от крайната сума в евро.

number_bitcoin = int(input())
number_chinese_yuan = float(input())
commission = float(input())

total_price_bitcoin_in_lv = number_bitcoin * 1168
total_price_chinese_yuan_in_lv = number_chinese_yuan * 0.15 * 1.76
total_sum = (total_price_bitcoin_in_lv + total_price_chinese_yuan_in_lv) - ((total_price_bitcoin_in_lv + total_price_chinese_yuan_in_lv) * commission / 100)
total_sum_in_euro = total_sum / 1.95
print(f'{total_sum_in_euro:.2f}')