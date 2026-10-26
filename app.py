
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def student():
    if request.method == "POST":
        name = request.form["name"].strip()
        department = request.form["department"].strip()

        if not name or not department:
            return "Please enter all details."

        return f"Student Name: {name}<br>Department: {department}"

    return """
    <h2>Student Management System</h2>
    <form method="POST">
        Student Name: <input type="text" name="name" required><br><br>
        Department: <input type="text" name="department" required><br><br>
        <input type="submit" value="Submit">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)

# Feature branch update
