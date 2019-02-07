from flask import Blueprint
from flask import render_template, request, redirect, url_for

com_bp = Blueprint('com_bp', __name__)



@com_bp.route('/')
def homePage():
    # Put any kind of python logic for any of the routes you make 
    # each route '/' or '/success' etc will be linked to the backend
    # Bassically  any a:href, form:action will be liked to a @app.route which will execute the code in it
    return render_template('main.html')

@com_bp.route('/success')
def showSuccessPage():
    return render_template('success.html')

@com_bp.route('/failed')
def showFailedPage():
    return render_template('failed.html')



