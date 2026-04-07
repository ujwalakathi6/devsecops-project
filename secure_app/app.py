import os
from flask import Flask, render_template

app = Flask(__name__)

# Load secrets from environment variables — do NOT hardcode secrets in source.
# If you need to demonstrate a missing secret, set `ADMIN_PASSWORD` in the
# environment of the running process locally or in CI; do not commit secrets.
#admin_password = os.environ.get('ADMIN_PASSWORD')
@app.route('/')
def home():
    # Do not display secret values in templates or error messages.
    if ADMIN_PASSWORD:
        return render_template(
            'index.html',
            vulnerable=True,
            error="Potential secret configured in environment (check deployment).",
        )

    return render_template('index.html', vulnerable=False)


if __name__ == "__main__":
    # Use Flask's dev server only for local testing. Port can be overridden
    # with the PORT environment variable.
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))