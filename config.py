import gate_api
from gate_api import ApiClient, Configuration, Order, SpotApi
from gate_api.exceptions import ApiException, GateApiException

import json
# satın alınabilir token listesini getir
listToken = "config.json"
try:
    with open(listToken) as f:
        d = json.load(f)
except ValueError:
    print("token lstesi dosyası açılamadı")
    print(ValueError)


# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = d["apiKey"],
    secret = d["secretKey"]
)

