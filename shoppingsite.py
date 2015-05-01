"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken.
"""


from flask import Flask, render_template, redirect, flash, session
import jinja2

import model


app = Flask(__name__)
app.secret_key = 'arimish'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melons = model.Melon.get_all()
    return render_template("all_melons.html",
                           melon_list=melons)


@app.route("/melon/<int:id>")
def show_melon(id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """

    melon = model.Melon.get_by_id(id)
    print melon
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart")
def shopping_cart():
    """Display content of shopping cart."""
    
    # cart = {}
    # total_melons = 0
    #MELON_QUERY = "SELECT common_name, price FROM melons WHERE id = ?"

    cart_dict = {}

    
    if "cart" in session:
        melon_ids = session["cart"]
        for id in melon_ids:
            melon = model.Melon.get_by_id(id)
            cart_dict[id] = cart_dict.get(id, 0) + 1
    

    # print cart_dict
    # print melon.common_name, melon.price, cart_dict[melon.id]

    # print dir(melon) I did this because it will show me all the things I can do to melon 

    # TODO: Display the contents of the shopping cart.
    #   - The cart is a list in session containing melons added

    return render_template("cart.html", 
                            common_name = melon.common_name,
                            price = melon.price,
                            num_melons = cart_dict[melon.id],
                            total_price = melon.price * cart_dict[melon.id])


@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Successfully added to cart'.
    """
    
    # TODO: Finish shopping cart functionality
    #   - use session variables to hold cart list
    
    session.setdefault('cart', [])
    session['cart'].append(id)   
    flash("Successfully added to cart!")

    return redirect("/cart")


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    # TODO: Need to implement this!

    return "Oops! This needs to be implemented"


@app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True)
