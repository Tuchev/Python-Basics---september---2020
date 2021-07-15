days = int(input())
type_of_room = input()
feedback = input()
price = 0
overnight = days - 1

if days < 10:
    if type_of_room == 'room for one person':
        price = 18.00
        if feedback == 'positive':
            price = price + price * 0.25
        elif feedback == 'negative':
            price = price - price * 0.10
    elif type_of_room == 'apartment':
        price = 25 * 0.7
        if feedback == 'positive':
            price = price + price * 0.25
        elif feedback == 'negative':
            price = price - price * 0.10
    elif type_of_room == 'president apartment':
        price = 35 * 0.10
        if feedback == 'positive':
            price = price + price * 0.25
        elif feedback == 'negative':
            price = price - price * 0.10

elif 10 <= days <= 15:
    if type_of_room == 'room for one person':
        price = 18.00
        if feedback == 'positive':
            price = price + price * 0.25
        elif feedback == 'negative':
            price = price - price * 0.10
    elif type_of_room == 'apartment':
        price = 25 * 0.65
        if feedback == 'positive':
            price = price + price * 0.25
        elif feedback == 'negative':
            price = price - price * 0.10
    elif type_of_room == 'president apartment':
        price = 35 * 0.85
        if feedback == 'positive':
            price = price + price * 0.25
        elif feedback == 'negative':
            price = price - price * 0.10

elif days > 15:
    if type_of_room == 'room for one person':
        price = 18.00
        if feedback == 'positive':
            price = price + price * 0.25
        elif feedback == 'negative':
            price = price - price * 0.10
    elif type_of_room == 'apartment':
        price = 25 * 0.50
        if feedback == 'positive':
            price = price + price * 0.25
        elif feedback == 'negative':
            price = price - price * 0.10
    elif type_of_room == 'president apartment':
        price = 35 * 0.80
        if feedback == 'positive':
            price = price + price * 0.25
        elif feedback == 'negative':
            price = price - price * 0.10
print(f'{(overnight * price):.2f}')