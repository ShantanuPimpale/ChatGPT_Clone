from flask import Flask, render_template, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore
import openai

openai.api_key = "API_KEY"

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("chatgpt-32a15-firebase-adminsdk-rky9h-bd2940b81e.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Define routes
@app.route('/')
def home():
    chats = db.collection('Data').stream()
    Mychat = []
    for chat in chats:
        Mychat.append(chat.to_dict())
        print(Mychat)
    return render_template("index.html", mychats=Mychat)

@app.route('/api', methods=["POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        
        # Query Firebase Firestore to get the answer
        doc_ref = db.collection('Data').where("question", "==", question).limit(1).get()
        if doc_ref:
            doc = doc_ref[0].to_dict()
            data = {"result": doc.get("answer")}
            return jsonify(data)
        else:
            response = openai.Completion.create(
                engine="davinci",
                prompt=question,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response)
            answer = response.choices[0].text.strip()
            data = {"question": question, "answer": answer}
            db.collection('Data').add({'question': question, 'answer': answer})
            return jsonify(data)
    
    # Default response if method is not POST
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss?"}
    return jsonify(data)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)



