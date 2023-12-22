from flask import Flask, render_template, request, jsonify
import random

data = {
    "what|explain|describe order": ["You can explore our wide range of products to make a purchase!", "To place an order, browse through our collection of items."],
    "how can i order?": ["You can easily order via our website or mobile app."],
    "orders": ["Here's the list of your placed orders."],
    "order": ["What product would you like to order?"],
    "items": ["We have a diverse selection of items available for purchase."],
    "hi|hello|hai|hlo": ["Welcome to our online store! How can I assist you today?", "Hello! How may I help you?"],
    "what are the specials?": [
        "Our specials include a variety of products such as electronics, clothing, home appliances, accessories, and more. We offer a wide range of items to cater to different needs."
    ],
    "i want|electronics|clothing|home appliances|accessories": [
        "Certainly, your order will be processed. Please expect a confirmation shortly."
    ],
    "show me electronics": [
        "We have a wide range of electronic products including smartphones, laptops, cameras, and more. Would you like to explore any specific electronics category?"
    ],
    "smartphones": [
        "Our smartphone collection includes the latest models from top brands like Apple, Samsung, OnePlus, and more. Feel free to browse our smartphone catalog."
    ],
    "laptops": [
        "We offer a diverse range of laptops suitable for various purposes, from gaming laptops to ultrabooks. Check out our selection of laptops."
    ],
    "what is e-commerce": [
        "E-commerce refers to the buying and selling of goods or services over the internet. It involves online transactions between businesses, consumers, or both. E-commerce allows customers to shop conveniently from anywhere at any time, and businesses can reach a global audience."
    ],
    "cameras": [
        "Explore our collection of high-quality cameras, including DSLRs, mirrorless cameras, and compact models, from leading brands in photography."
    ],
    "what is the price?": ["The price varies for different products. You can check the specific product page for accurate pricing information."],
    "here is the bill amount": ["Thank you for shopping with us! Your payment has been received. Have a great day!"]
}

app = Flask(__name__)

# Routing
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input'].lower()
    inn = False
    res = ""
    for keys, value in data.items():
        keys = keys.split()
        for key in keys:
            key = key.split('|')
            if any(k in user_input for k in key):
                inn = True
            else:
                inn = False
                break
        if inn:
            res = random.choice(value)
            break
    if inn:
        return jsonify({'bot_response': res})
    else:
        return jsonify({'bot_response': "I couldn't understand your request!"})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
