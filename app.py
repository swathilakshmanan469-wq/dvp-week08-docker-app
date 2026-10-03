from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DVP Week 08</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
                background-color: #f4f7f9;
            }

            h1 {
                color: #2496ed;
            }

            p {
                font-size: 20px;
                color: #333;
            }

            .box {
                background: white;
                padding: 40px;
                margin: auto;
                width: 500px;
                border-radius: 15px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>DVP Week 08 - Dockerized Web Application</h1>
            <p>Hello from my Docker container! 🐳</p>
            <p>Python Flask Web Application</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)