#!/usr/bin/env python3
"""
Project 18 – Wireless Auditing Dashboard
Shows captured handshakes and crack status.
"""
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/status')
def status():
    has_handshake = os.path.exists("handshake.cap")
    files = os.listdir(".") if has_handshake else []
    return jsonify({
        "handshake": has_handshake,
        "files": files[:10]
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)