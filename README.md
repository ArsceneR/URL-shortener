
# URL Shortener

A simple Flask-based web application to shorten URLs, store them in a PostgreSQL database, and redirect users from short URLs to the original links.

## Features
- Shorten long URLs to compact, shareable links
- Store and retrieve URL mappings using PostgreSQL
- Easily extensible and configurable
## Illustration

![Screenshot of the app UI](app/static/Screenshot%202025-06-04%20at%2012.09.19%E2%80%AFPM.png)
## Requirements
- Python 3.8+
- PostgreSQL (running locally or remotely)
- pipenv or pip for dependency management

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/URL-shortener.git
cd URL-shortener
```

### 2. Install dependencies
Using pipenv:
```bash
pipenv install
```
Or using pip:
```bash
pip install -r requirements.txt
```

### 3. Configure the application
Create & Edit `.env` with your PostgreSQL credentials and app settings:
```
DomainName = localhost
PORT: 8000
Protocol = http
SHORT_URL_LENGTH = 10

Database = db_name
User = user
Password = password
Host = 127.0.0.1
Port = 5432
```

### 4. Start PostgreSQL
Make sure your PostgreSQL server is running and accessible.
Steps: https://www.postgresql.org/docs/current/tutorial-start.html

To check if PostgreSQL is running:
```bash
pg_isready
```
To start on macOS (Homebrew):
```bash
brew services start postgresql
```

### 5. Run the app
```bash
python app.py
```
Or use the VS Code debugger with the provided `.vscode/launch.json`.

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

If you want to access from another device on your network, use your local IP and set `host='0.0.0.0'` in `app.py`.

## Usage
- Enter a long URL in the input field and click "Shorten".
- Copy the generated short URL and share it.
- Visiting the short URL will redirect to the original link.

### Example
1. Input: `https://www.example.com/very/long/url`
2. Output: `http://{host}:{port}/abc123`
3. Visiting `http://{host}:{port}/abc123` redirects to the original URL.

## Project Structure
```

URL-shortener/
├── app/                           # Application package
│   ├── __init__.py                # App factory (create_app) lives here
│   ├── main.py                    # Optional entry point (can also use Flask CLI)
│   ├── routes/                    # Blueprint-based routes
│   │   └── home.py                
│   ├── pg_database.py             # PostgreSQL database integration
│   ├── short_url_generator.py     # URL shortening logic
│
├── .envSample                     # Example environment variables file
├── .gitignore                     # Git ignore rules
├── requirements.txt               # Project dependencies
├── config.py                      # Config classes (DevConfig, ProdConfig, etc.)
├── README.md                      # Project documentation


```

## Customization
- Change the short URL length in `.env` (`Length` parameter).
- Update the domain or protocol as needed.
- Add your own favicon or branding in `static/` and `templates/`.

- To use a custom port, change the `port` in `app.py` or in your VS Code `launch.json` or use the CLI to run the app.

## Advanced Usage
- Containerize the application and deploy this app to Heroku, Render, or any cloud provider that supports Flask and PostgreSQL.
- For production, use a WSGI server like Gunicorn and set `debug=False`.

## Troubleshooting / Common Issues
- **403 Forbidden:** Make sure Flask is running and you are using the correct port. Try both `127.0.0.1:5000` and `localhost:5000`.
- **Database errors:** Ensure PostgreSQL is running and credentials in the env file are correct. Try connecting with `psql` to verify.
- **Port 5000 in use on Mac:** Bind app to another port(like 8000) or follow steps here: [StackOverflow: Port 5000 in use](https://stackoverflow.com/questions/72369320/why-always-something-is-running-at-port-5000-on-my-mac)

## Security Notes
- This app is for educational/sys design demo purposes . For production, add input validation, HTTPS, and user authentication as needed.



- **Macboook Port 5000 Issue:** : Bind app to another port or follow steps here
 https://stackoverflow.com/questions/72369320/why-always-something-is-running-at-port-5000-on-my-mac
## Contributing
Pull requests and issues are welcome! Please open an issue to discuss your ideas or report bugs.


