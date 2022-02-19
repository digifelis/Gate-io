from __future__ import print_function
from urllib import response
import config as cfg
import gate_api
from gate_api import ApiClient, Configuration, Order, SpotApi
from gate_api.exceptions import ApiException, GateApiException
import json
api_client = gate_api.ApiClient(cfg.configuration)

def total_balance(currency):
    api_instance = gate_api.WalletApi(api_client)
    try:
        # Retrieve user's total balances
        api_response = api_instance.get_total_balance(currency=currency)
        return api_response.details["spot"]
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
        return ex.message
    except ApiException as e:
        return "Exception when calling WalletApi->get_total_balance: %s\n" % e

#print(total_balance("USD"))

def get_currency_last_price(currency_pair):
    api_instance = gate_api.SpotApi(api_client)
    try:
        # Get details of a specific currency
        api_response = api_instance.list_tickers(currency_pair=currency_pair)
        return api_response[0].last
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
        return ex.message
    except ApiException as e:
        return "Exception when calling SpotApi->get_currency: %s\n" % e

#print(get_currency_last_price("GT_USDT"))

def get_balance(currency):
    api_instance = gate_api.SpotApi(api_client)
    try:
        # Get details of a specific currency
        api_response = api_instance.list_spot_accounts(currency=currency)
        return api_response[0].available
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
        return ex.message
    except ApiException as e:
        return "Exception when calling SpotApi->get_currency: %s\n" % e

#print(get_balance("USDT"))

def create_order(currency_pair, order_amount, last_price, side):
    api_instance = gate_api.SpotApi(api_client)
    order = gate_api.Order(amount=str(order_amount), price=last_price, side=side, currency_pair=currency_pair)
    try:
        api_response = api_instance.create_order(order)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
        return ex.message
    except ApiException as e:
        return "Exception when calling SpotApi->get_currency: %s\n" % e

#print(create_order("GT_USDT", 1, get_currency_last_price("GT_USDT"), "buy"))

def list_orders(currency_pair, status = "open", side = 'buy'):
    account = 'spot'
    page=1
    limit=100
    api_instance = gate_api.SpotApi(api_client)
    
    try:
        api_response = api_instance.list_orders(currency_pair, status, page=page, limit=limit, account=account, side=side)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
        return ex.message
    except ApiException as e:
        return "Exception when calling SpotApi->get_currency: %s\n" % e

#print(list_orders("GT_USDT", "open", "buy"))

def cancel_order(order_id, currency_pair):
    account = 'spot'
    api_instance = gate_api.SpotApi(api_client)
    try:
        api_response = api_instance.cancel_order(order_id, currency_pair, account=account)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
        return ex.message
    except ApiException as e:
        return "Exception when calling SpotApi->get_currency: %s\n" % e

#print(cancel_order("12345", "GT_USDT"))

def create_withdraw(currency, address, amount):
    api_instance = gate_api.WithdrawalApi(api_client)
    ledger_record = gate_api.LedgerRecord(currency=currency, address=address, amount=amount)
    try:
        api_response = api_instance.withdraw(ledger_record)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
        return ex.message
    except ApiException as e:
        return "Exception when calling SpotApi->get_currency: %s\n" % e

#print(create_withdraw("USDT", "1HkxtBAMrA3tP5ENnYY2CZortjZvFDH5Cs", 1))

def cancel_withdraw(withdraw_id):
    api_instance = gate_api.WithdrawalApi(api_client)
    try:
        api_response = api_instance.cancel_withdrawal(withdraw_id)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
        return ex.message
    except ApiException as e:
        return "Exception when calling SpotApi->get_currency: %s\n" % e

#print(cancel_withdraw("210496"))