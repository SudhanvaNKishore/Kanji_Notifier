import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template

# Sample data
sample_data = {
    "username": "John Doe",
    "kanjis": [
        {"character": "日", "meaning": "Sun", "example": "今日は晴れです。"},
        {"character": "月", "meaning": "Moon", "example": "月が綺麗です。"},
    ],
    "user_preferences": "Nature, Astronomy",
    "unsubscribe_link": "http://example.com/unsubscribe"
}

# Load the template
template_str = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }
        .container {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #4CAF50;
        }
        .kanji {
            font-size: 24px;
            font-weight: bold;
            color: #000;
        }
        .footer {
            font-size: 12px;
            text-align: center;
            color: #777;
        }
        .unsubscribe {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #f44336;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .preferences {
            font-size: 14px;
            margin-top: 20px;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Kanji Notifier - Your Daily Dose of Kanjis!</h1>
        <p>Dear {{ username }},</p>
        <p>Thank you for subscribing to our Kanji Notifier. Here are your selected Kanjis for today:</p>
        <ul>
            {% for kanji in kanjis %}
            <li>
                <span class="kanji">{{ kanji.character }}</span> - {{ kanji.meaning }}
                <br>
                Example: {{ kanji.example }}
            </li>
            {% endfor %}
        </ul>
        <p class="preferences">You have chosen to receive kanjis related to: {{ user_preferences }}</p>
        <p>Keep learning and expanding your kanji knowledge!</p>
        <div class="footer">
            <p>If you wish to unsubscribe, please click the link below:</p>
            <a href="{{ unsubscribe_link }}" class="unsubscribe">Unsubscribe</a>
        </div>
    </div>
</body>
</html>
"""

# Render the template
template = Template(template_str)
rendered_email = template.render(sample_data)

# Email configuration
from_email = "your_mail_id"
to_email = "user_mail_id"
subject = "Your Daily Kanji Notification"

# Create message container
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

# Attach the HTML content
msg.attach(MIMEText(rendered_email, 'html'))

# Send the email
try:
    # Connect to the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, "your_password")  # Use an app-specific password if using Gmail

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()