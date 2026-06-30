from flask import Flask, request, render_template_string

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
        ad = f"Try {product} today! High quality and perfect for your needs."
    return render_template_string(HTML, ad=ad)

if __name__ == "__main__":
    app.run(debug=True)
