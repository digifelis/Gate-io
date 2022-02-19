import func as task

amount = 100
currency = "USDT"
currency_pair = "GT_USDT"
#satın alma süreci
last_price = task.get_currency_last_price(currency_pair)
balance = task.get_balance(currency)
if last_price*amount < balance:
    task.create_order(currency_pair, amount, last_price, "buy")
else:
    print("balance not enough")