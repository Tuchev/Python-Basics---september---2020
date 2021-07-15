x = float(input())
y = float(input())
h = float(input())

door = 1.2 * 2
windows = 1.5 * 1.5

predna_stena = (x * x) - door
zadna_stena = x * x
stranichni_steni = 2 * (x * y) - 2 * windows
vsichko_stranici = predna_stena + zadna_stena + stranichni_steni

pokriv_stranichni_chasti = 2 * (x * y)
pokriv_predna_zadna_chast = 2 * (x * h / 2)
celiq_pokriv = pokriv_predna_zadna_chast + pokriv_stranichni_chasti

green_paint = vsichko_stranici / 3.4
red_paint = celiq_pokriv / 4.3
print(f'{green_paint: .2f}')
print(f'{red_paint: .2f}')