from configparser import ConfigParser
from flask import Flask, redirect, render_template, request
from pg_database import PostgreDB
from short_url_generator import URLShortener

app = Flask(__name__)

config = ConfigParser()
config.read('config.ini')

DOMAIN_NAME = config['MAIN']['DomainName']
LENGTH = int(config['MAIN']['Length'])
PROTOCOL = config['MAIN']['Protocol']
DB_CONFIG = dict(config['DATABASE'].items())

url_shortener = URLShortener(length=LENGTH)
database = PostgreDB(DB_CONFIG)


@app.route('/favicon.ico')
def favicon():
    return '', 204 

@app.route('/', methods=['GET', 'POST'])
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
    if request.method == 'POST':
        url = request.values['fullUrl'].strip()
        short_url = database.check_data_exist(original=url)
        if not short_url:
            short_url = url_shortener.shorten_url(url)
            if not short_url:
                result = 'Validation Failure. This may be an incorrect URL.'
            else:
                database.add_data((short_url, url))
                result = f"{PROTOCOL}://{DOMAIN_NAME}/{short_url}"
        else:
            result = f"{PROTOCOL}://{DOMAIN_NAME}/{short_url}"
        return render_template('index.html', result=result)
    else:
        database.create_table()
        return render_template('index.html')


@app.route('/<url>')
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
    result = database.check_data_exist(shorten=url)
    if result:
        return redirect(result)
    else:
        return 'PAGE DOES NOT EXIST.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
