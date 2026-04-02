import os
from flask import Flask, render_template

app = Flask(__name__)

# FACULTY DEMO: The Vulnerability
# To show a "Clean" site, comment out the line below.
# Bandit will flag this as B105 (Hardcoded password) with HIGH severity
ADMIN_PASSWORD = "AKIA5S6D7F8G9H0J1K2L_SECRET_KEY_EXPOSED_123456789"

@app.route('/')
def home():
    # We check if the dangerous variable exists
    has_vulnerability = False
    error_msg = ""
    
    if 'ADMIN_PASSWORD' in globals() and ADMIN_PASSWORD:
        has_vulnerability = True
        error_msg = f"CRITICAL: Hardcoded Credential Detected ('{ADMIN_PASSWORD}')"

    return render_template('index.html', 
                           vulnerable=has_vulnerability, 
                           error=error_msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)