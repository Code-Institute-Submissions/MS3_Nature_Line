import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# Landing page
@app.route("/home")
def home():
    if 'user' in session:
        return redirect(url_for("profile", username = session["user"]))

    return render_template("index.html")


#Register functionality
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})
        # Check if username already exists
        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "type": request.form.get("user_type").lower()
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull!")
        return redirect(url_for('profile', username=session["user"]))
    return render_template("register.html")


#Login functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})
        # Check if username/password is correct
        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] =  request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for('profile', username=session["user"]))
            else:
                flash("Incorrect Username and/or Password!")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password!")
            return redirect(url_for("login"))
    return render_template("login.html")


#Logout functionality
@app.route("/logout")
def logout():
    flash("You have bee successfully loged out!")
    session.pop("user")
    return redirect(url_for("login"))


#Profile functionality
@app.route("/profile/<username>", methods = ["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    curr_user = mongo.db.users.find_one({"username": session["user"]})
    products_sold = mongo.db.products_sold.find()
    if session["user"]:
        return render_template("profile.html", username=username, curr_user=curr_user, products_sold=products_sold)

    return redirect(url_for("login"))


#Add product functionality
@app.route("/add_product", methods = ["GET", "POST"])
def add_product():
    if request.method == "POST":
        product_sold = {
            "category": request.form.get("category"),
            "name": request.form.get("name"),
            "price": request.form.get("price"),
            "quantity": request.form.get("quantity"),
            "sold_by": session["user"]
        }
        mongo.db.products_sold.insert_one(product_sold)
        flash("Product successfully added!")
        return redirect (url_for("profile", username=session["user"]))
    product_cat = mongo.db.product_categories.find().sort("category", 1)
    return render_template("add_product.html", product_cat=product_cat)


#Edit product functionality
@app.route("/edit_product/<product_id>", methods=["GET","POST"])
def edit_product(product_id):
    if request.method == "POST":
        product_update = {
            "category": request.form.get("category"),
            "name": request.form.get("name"),
            "price": request.form.get("price"),
            "quantity": request.form.get("quantity"),
            "sold_by": session["user"]
        }
        mongo.db.products_sold.update({"_id": ObjectId(product_id)}, product_update)
        flash("Product successfully updated!")
        return redirect (url_for("profile", username=session["user"]))
    product_sold = mongo.db.products_sold.find_one({"_id": ObjectId(product_id)})
    product_cat = mongo.db.product_categories.find().sort("category", 1)
    return render_template("edit_product.html", product_sold=product_sold,product_cat=product_cat)


@app.route("/delete_product/<product_id>")
def delete_product(product_id):
    mongo.db.products_sold.remove({"_id": ObjectId(product_id)})
    flash("Product successfully deleted!")
    return redirect (url_for("profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
