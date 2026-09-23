from  flask import Flask, render_template, request
from main import get_article

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/article/<int:article_id>")
def blog(article_id):
    article = get_article(article_id)
    
    return render_template("blog.html", articles=article)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        username = request.form.get("username").lower()
        password = request.form.get("password")
        print(password)
        print(username)

        admin_username = "emodoh"
        admin_password = "1234" 

        if username == admin_username:
            if password == admin_password:
                return render_template("admin.html")

        else:
            return "incorrect password or username."




    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

