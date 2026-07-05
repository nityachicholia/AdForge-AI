from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    ad = ""

    if request.method == "POST":
        product = request.form["product"]

        ads = [
            f"Try {product} today! High quality and perfect for your needs.",
            f"Looking for the best {product}? Get yours now!",
            f"{product} - Smart choice for smart people.",
            f"Upgrade your lifestyle with {product}."
        ]

        ad = random.choice(ads)

    return render_template("index.html", result=ad)

if __name__ == "__main__":
    app.run(debug=True)
