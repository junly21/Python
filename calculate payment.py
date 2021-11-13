def weeklyPay(rate,hour):
  money=0
  if hour>30:
    money = 30*rate+(hour-30)*1.5*rate
  else:
    money = hour*rate
  return money


rate = int(input("input rate"))
hour = int(input("input hour you work"))
print("the payment is" + str(weeklyPay(rate,hour)))