import os
from flask import Flask, render_template

app = Flask(__name__)

# FACULTY DEMO: This is the "Security Trap"
ADMIN_PASSWORD = "Sreenidhi_Admin_123" 

@app.route('/')
def home():
    # This looks for index.html inside the 'templates' folder
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)