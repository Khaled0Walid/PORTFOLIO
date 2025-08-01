from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        # You can save or process this data as needed
        return f"Thanks {name}, your message was received!"
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
