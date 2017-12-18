#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['GET'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "shipping.cost":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("shipping-zone")

    cost = {'Economic':http://www.moneycontrol.com/news/economy/budget-may-increase-interest-deductionhome-loans-by-rs-50k_8206301.html, 'Current Affairs':http://www.moneycontrol.com/news/current-affairs/ccpa-recommends-holdingbudget-sessionjanuary-31_8200681.html, 'Economic':http://www.moneycontrol.com/news/economy/no-constitutional-clash-polls-happen-close-to-budget-ranina_8209741.html, 'Politics':http://www.moneycontrol.com/news/politics/opposition-happybudget-date-asks-postponement_8214961.html, 'Economy':http://www.moneycontrol.com/news/economy/union-budget-country-state-specific-venkaiah-naidu_8223681.html}

    speech = "The cost of shipping to " + zone + " is " + str(cost[zone]) + " euros."

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
