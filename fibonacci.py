from flask import Flask, render_template, request

app = Flask(__name__)

# Create a function that generates the Fibonacci numbers
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]  # Ensure we return exactly 'n' numbers

@app.route("/", methods=["GET", "POST"])
def index():
    results = None  # Initialize results as None
    if request.method == "POST":
        try:
            n = int(request.form["n"])
            if n > 0:
                results = generate_fibonacci(n)
            else:
                results = ["Please enter a positive integer."]
        except ValueError:
            results = ["Invalid input. Please enter a valid integer."]
    return render_template("index.html", Results=results)

if __name__ == "__main__":
    app.run(debug=True)
