from flask import render_template, redirect, request, session, url_for

def index_page():
    return render_template("index.html")

def login_page():
    username = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Учебный пример проверки логина и пароля
        # В реальных приложениях проверка выполняется с помощью KDF-функций
        if username == "admin" and password == "pass":
            session["username"] = username
            return redirect(url_for("index_page"))
    return render_template("login.html", username=username)

def logout():
    session.pop("username")
    return redirect(url_for("index_page"))