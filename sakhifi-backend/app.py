from flask import Flask, request, jsonify
from flask_cors import CORS   # <-- Import it here
from firebase_config import db
app = Flask(__name__)
CORS(app)                     # <-- Add this line

@app.route('/')
def hello():
    return "Hello from SakhiFi!"

@app.route('/api/chatbot/loan', methods=['POST'])
def loan_chatbot():
    data = request.get_json()
    user_question = data.get('question', '')
    recommendation = "Based on your income, a microfinance loan might work best."
    return jsonify({'recommendation': recommendation})

@app.route('/api/chatbot/finance', methods=['POST'])
def finance_chatbot():
    data = request.get_json()             # read JSON from the request body
    user_question = data.get('question', '')
    
    # Replace this with real financial logic or AI model
    # For now, a placeholder text:
    recommendation = "Track your expenses, focus on saving 20% of your monthly income."
    return jsonify({'recommendation': recommendation})

@app.route('/api/shg', methods=['GET'])
def get_shg_details():
    docs = db.collection('shgDetails').stream()
    results = []
    for doc in docs:
        results.append(doc.to_dict())
    return jsonify(results)

@app.route('/api/centers', methods=['GET'])
def get_centers():
    docs = db.collection('centers').stream()
    results = []
    for doc in docs:
        # doc.to_dict() is your Firestore document data
        center_data = doc.to_dict()
        center_data['id'] = doc.id  # If you want the doc ID as well
        results.append(center_data)
    return jsonify(results)

if __name__ == "__main__":
    print("Flask is starting on http://127.0.0.1:5000")
    app.run(debug=True)
 # The 'db' from the file above

app = Flask(__name__)


