from flask import appcontext_popped
from FlaskReact import init_app

# Imports and starts Flask App
app = init_app()

if __name__ == "__main__":
    app.run()
