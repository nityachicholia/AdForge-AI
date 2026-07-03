from flask import Flask, request, render_template_string
import random

print("NEW APP RUNNING")

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AdForge AI</title>
</head>
<body>
    <h1>AdForge AI</h1>

    <form method="POST">
        <input type="text" name="product" placeholder="Product Name" required>
        <button type="submit">Generate Ad</button>
    </form>

    {% if ad %}
    <h2>Generated Ad:</h2>
    <p>{{ ad }}</p>
    {% endif %}

</body>
</html>
"""

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

    return render_template_string(HTML, ad=ad)

if __name__ == "__main__":
    app.run(debug=True)
