
from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return "Flask webhook is running wait!"

    data = request.get_json()

    source_currency = data['queryResult']['parameters']['unit-currency'][0]['currency']
    amount = data['queryResult']['parameters']['unit-currency'][0]['amount']
    target_currency = data['queryResult']['parameters']['currency-name'][0]

    print("Source:", source_currency)
    print("Amount:", amount)
    print("Target:", target_currency)

    final_amount = fetch_conversion_amount(
        source_currency,
        target_currency,
        amount
    )

    print("Final Amount:", final_amount)

    response = {
        "fulfillmentText": "{} {} is {:.2f} {}".format(
            amount,
            source_currency,
            final_amount,
            target_currency
        )
    }

    return response


def fetch_conversion_amount(source, target, amount):

    url = "https://v6.exchangerate-api.com/v6/{}/pair/{}/{}/{}".format(
        API_KEY,
        source,
        target,
        amount
    )

    response = requests.get(url)
    response = response.json()

    print(response)

    return response['conversion_result']


if __name__ == "__main__":
    app.run(debug=True, port=5000)