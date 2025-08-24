
from flask import Blueprint, redirect, render_template, request, current_app


home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET', 'POST'])
def home():
    """
    Home page.

    If accessed via POST request, it shortens the URL and stores it in the database.
    If accessed via GET request, it displays the homepage.

    Returns:
        str: Rendered HTML template.

    Raises:
        None.
    """
    database = current_app.database

    if request.method == 'POST':
        url = request.values['fullUrl'].strip()
        short_url = database.fetch_url_if_exists(original=url)
        if not short_url:
            short_url = current_app.url_shortener.shorten_url(url)
            if not short_url:
                result = 'Validation Failure. This may be an incorrect URL.'
            else:
                database.add_data((short_url, url))
                result = f"{current_app.config["PROTOCOL"]}://{current_app.config["DOMAIN_NAME"]}/{short_url}"
        else:
            result = f"{current_app.config["PROTOCOL"]}://{current_app.config["DOMAIN_NAME"]}/{short_url}"
        return render_template('index.html', result=result)
    else:
        database.create_table()
        return render_template('index.html')


@home_bp.route('/<url>')
def url_redirect(url):
    """
    Redirect to original URL.

    Args:
        url (str): The shortened URL.

    Returns:
        str: Redirection to the original URL if found, otherwise an error message.

    Raises:
        None.
    """
    result = current_app.database.fetch_url_if_exists(shorten=url)
    if result:
        return redirect(result)
    else:
        return 'PAGE DOES NOT EXIST.'



@home_bp.route('/favicon.ico')
def favicon():
    return '', 204 