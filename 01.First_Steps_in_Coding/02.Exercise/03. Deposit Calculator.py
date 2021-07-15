#1.	Депозирана сума – реално число;
#2.	Срок на депозита(в месеци) – цяло число;
#3.	Годишен лихвен процент – реално число;
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
deposit_sum = float(input())
term_of_deposit = int(input())
gpr = float(input())
total_sum = deposit_sum + (term_of_deposit * (deposit_sum * gpr / 100) / 12)
print(total_sum)