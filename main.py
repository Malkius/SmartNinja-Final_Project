import requests
from flask import Flask, render_template, request, make_response, redirect, url_for
from models import User, db

app = Flask(__name__)
db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        email_address = request.cookies.get("email")
        if email_address:
            user = db.query(User).filter_by(email=email_address).first()
        else:
            user = None
        return render_template("index.html", user=user)

    elif request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")

        print(nombre)
        print(email)

        user = User(name=nombre, email=email)
        db.add(user)
        db.commit()

        response = make_response(redirect(url_for("index")))
        response.set_cookie("email", email)

        return response


@app.route("/logout")
def logout():
    response = make_response(redirect(url_for("index")))
    response.set_cookie("email", expires=0)

    return response


@app.route("/enviar", methods=["GET", "POST"])
def enviar():
    if request.method == "GET":
        email_address = request.cookies.get("email")
        if email_address:
            user = db.query(User).filter_by(email=email_address).first()
        else:
            user = None
        return render_template("enviar.html", user=user)

    elif request.method == "POST":
        name_destiny = request.form.get("nombre_destinatario")
        last_name = request.form.get("apellido_destinatario")
        email_destiny = request.form.get("email_destino")
        message_sent = request.form.get("mensaje_enviado")

        print(name_destiny)
        print(last_name)
        print(email_destiny)
        print(message_sent)

        user = User(name_destiny=name_destiny, last_name=last_name,
                    email_destiny=email_destiny, message_sent=message_sent)

        db.add(user)
        db.commit()

        response = make_response(redirect(url_for("index")))

        return response


@app.route("/tiempo", methods=["GET"])
def tiempo():
    lang = "es"
    query = "Malaga,es"
    api_key = "8f99c83b162f4d45d27e6034964abebe"
    unit = "metric"
    url = "https://api.openweathermap.org/data/2.5/weather?lang={0}&q={1}&units={2}&appid={3}"\
        .format(lang, query, unit, api_key)
    response = requests.get(url=url)
    return render_template("tiempo.html", data=response.json())


if __name__ == '__main__':
    app.run(debug=True)
