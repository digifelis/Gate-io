import func as task

amount = 100
currency = "GT"
currency_pair = "GT_USDT"
#satın alma süreci
last_price = task.get_currency_last_price(currency_pair)
balance = task.get_balance(currency)
print(float(balance))

if amount < float(balance):
    task.create_order(currency_pair, amount, last_price, "sell")
else:
    print("balance not enough")

