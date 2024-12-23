from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash
import os
import yfinance as yf

app = Flask(__name__)
CORS(app)  # Engedélyezi a frontend kéréseit

# MongoDB kapcsolat
try:
    mongo_uri = os.getenv("MONGO_URI", "mongodb://admin:admin@localhost:27017/portfolio?authSource=admin")
    client = MongoClient(mongo_uri)
    db = client["portfolio"]  # Adatbázis megadása
    users_collection = db["users"]
except Exception as e:
    print("Error connecting to MongoDB:", e)
    exit()


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = db.users.find_one({"username": username})

    if user and check_password_hash(user['password'], password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if db.users.find_one({"username": username}):
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    db.users.insert_one({"username": username, "password": hashed_password})
    return jsonify({"message": "User added successfully"}), 201


@app.route('/stock', methods=['GET'])
def get_stock():
    symbol = request.args.get('symbol', 'AAPL')

    try:
        stock_data = yf.Ticker(symbol)
        hist = stock_data.history(period="1d", interval="5m")

        if hist.empty or 'Open' not in hist.columns:
            return jsonify({'error': 'Invalid symbol or no data available'}), 400

        latest_data = hist.iloc[-1]
        return jsonify({
            'symbol': symbol,
            'price': round(latest_data['Open'], 2),
            'time': latest_data.name.strftime('%Y-%m-%d %H:%M:%S')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
