from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Fungsi untuk membaca feedback dari file JSON
def load_feedback():
    try:
        with open("feedback.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Fungsi untuk menyimpan feedback ke file JSON
def save_feedback(feedback_list):
    with open("feedback.json", "w") as file:
        json.dump(feedback_list, file, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_feedback", methods=["GET"])
def get_feedback():
    feedback_list = load_feedback()
    return jsonify(feedback_list)

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json()
    feedback_list = load_feedback()
    
    new_feedback = {"name": data["name"], "message": data["message"]}
    feedback_list.append(new_feedback)
    
    save_feedback(feedback_list)
    
    return jsonify({"success": True, "message": "Feedback berhasil disimpan!"})

if __name__ == "__main__":
    app.run(debug=True)
