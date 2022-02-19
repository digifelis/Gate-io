import func as task

amount = 100
currency = "ALPA"
address = "1HkxtBAMrA3tP5ENnYY2CZortjZvFDH5Cs"
response = task.create_withdraw(currency, address, amount)
print(response)