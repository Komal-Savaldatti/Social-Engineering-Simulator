from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)

# ==========================================
# EMAIL CONFIGURATION
# ==========================================

EMAIL_ADDRESS = "balavandi0910@gmail.com"

EMAIL_PASSWORD = "dlwrrxgguytcvxxh"

TARGET_EMAIL = "balavando0910@gmail.com"


# ==========================================
# SEND EMAIL FUNCTION
# ==========================================

def send_simulation_email():

    subject = "Social Engineering Awareness Simulation"

    body = """
Hello,

This is a Social Engineering Awareness Simulation.

Click the link below:

http://127.0.0.1:5000/simulation

Regards,
Social Engineering Simulator Team
"""

    msg = MIMEText(body)

    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TARGET_EMAIL

    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        server.send_message(msg)

        server.quit()

        print("Email Sent Successfully")

    except Exception as e:

        print("Error Sending Email")
        print(e)


# ==========================================
# SEND EMAIL AUTOMATICALLY
# ==========================================

send_simulation_email()


# ==========================================
# DASHBOARD PAGE
# ==========================================

@app.route('/')
def dashboard():

    return render_template('dashboard.html')


# ==========================================
# PROJECT INFO PAGE
# ==========================================

@app.route('/project-info')
def project_info():

    return render_template('project_info.html')


# ==========================================
# SIMULATION LOGIN PAGE
# ==========================================

@app.route('/simulation', methods=['GET', 'POST'])
def simulation():

    if request.method == 'POST':

        username = request.form['username']

        with open("logs.txt", "a") as file:

            file.write(
                f"Username: {username} | Password Entered: Yes | Time: {datetime.now()}\n"
            )

        return """

        <html>

        <head>

        <title>Simulation Result</title>

        <style>

            body{
                background:#0f172a;
                color:white;
                text-align:center;
                font-family:Arial;
                padding-top:100px;
            }

            .box{
                background:#1e293b;
                width:60%;
                margin:auto;
                padding:40px;
                border-radius:15px;
            }

            h1{
                color:#22c55e;
            }

            a{
                color:#38bdf8;
                text-decoration:none;
                font-size:20px;
            }

        </style>

        </head>

        <body>

            <div class="box">

                <h1>Simulation Completed</h1>

                <p>
                    This was a Social Engineering Awareness Simulation.
                </p>

                <p>
                    Never enter passwords on suspicious websites.
                </p>

                <br>

                <a href="/logs">
                    View Logs
                </a>

            </div>

        </body>

        </html>

        """

    return """

    <html>

    <head>

    <title>Login Page</title>

    <style>

        body{
            background:#111827;
            color:white;
            font-family:Arial;
            text-align:center;
            padding-top:100px;
        }

        .box{
            background:#1f2937;
            width:40%;
            margin:auto;
            padding:40px;
            border-radius:15px;
        }

        input{
            width:80%;
            padding:12px;
            margin:10px;
            border:none;
            border-radius:8px;
        }

        button{
            padding:12px 30px;
            background:#2563eb;
            color:white;
            border:none;
            border-radius:8px;
            font-size:18px;
        }

    </style>

    </head>

    <body>

        <div class="box">

            <h1>Login Page</h1>

            <form method="POST">

                <input type="text"
                       name="username"
                       placeholder="Enter Username"
                       required>

                <br>

                <input type="password"
                       name="password"
                       placeholder="Enter Password"
                       required>

                <br><br>

                <button type="submit">
                    Login
                </button>

            </form>

        </div>

    </body>

    </html>

    """


# ==========================================
# LOGS PAGE
# ==========================================

@app.route('/logs')
def logs():

    try:

        with open("logs.txt", "r") as file:

            logs_data = file.read()

    except:

        logs_data = "No logs available"

    return render_template(
        "logs.html",
        logs_data=logs_data
    )


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)