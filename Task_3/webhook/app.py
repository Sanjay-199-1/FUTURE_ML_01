from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent = req.get('queryResult').get('intent').get('displayName')
    
    if intent == 'order_status':
        return jsonify({
            'fulfillmentText': 'Your order is in transit and will be delivered tomorrow.'
        })
    elif intent == 'return_policy':
        return jsonify({
            'fulfillmentText': 'You can return your item within 7 days via the "My Orders" section.'
        })
    else:
        return jsonify({
            'fulfillmentText': 'Sorry, I didn’t get that.'
        })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
