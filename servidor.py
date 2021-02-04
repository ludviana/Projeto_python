from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")


@app.route("/", methods=["GET", "POST"])
def home():
    global num2, num1
    if request.method == "GET":
        return render_template("index.html")
    else:
        if request.form["num1"] == "":
            num1 = int(0)
        elif request.form["num1"] != "":
            num1 = int(request.form["num1"])

        if request.form["num2"] == "":
            num2 = int(0)
        elif request.form["num2"] != "":
            num2 = int(request.form["num2"])

        operador = request.form["opc"]

        if operador == "soma":
            soma = num1 + num2
            return str(soma)
        elif operador == "subt":
            subt = round(num1 - num2, 2)
            return str(subt)
        elif operador == "mult":
            mult = round(num1 * num2, 2)
            return str(mult)
        elif operador == "divi":
            divi = round(num1 / num2, 2)
            return str(divi)


@app.errorhandler(404)
def not_found(error):
    return render_template("erro.html")


app.run(port=8080, debug=True)
