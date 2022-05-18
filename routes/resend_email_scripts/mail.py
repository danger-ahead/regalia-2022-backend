from re import T
import requests
import env_config


def send_mail(mail, name, uid, allowed):
    try:
        html_file = open("routes/resend_email_scripts/templates/pass.html")
        html_obj = str(html_file.read())
        html_file.close()

        html_obj = html_obj.replace("***NAME***", "Hi " + name.split(" ")[0] + ",")
        html_obj = html_obj.replace("***UID***", uid.upper())

        if allowed == "1":
            html_obj = html_obj.replace("***ALLOWED***", "Single Entry Only")

        elif allowed == "2":
            html_obj = html_obj.replace("***ALLOWED***", "+1 allowed")

        elif allowed == "3":
            html_obj = html_obj.replace("***ALLOWED***", "+2 allowed")

        t = requests.post(
            "https://api.eu.mailgun.net/v3/" + env_config.mailgun_domain + "/messages",
            auth=("api", env_config.mailgun_key),
            files=[
                (
                    "attachment",
                    open("routes/resend_email_scripts/templates/pass.png", "rb"),
                ),
                (
                    "attachment",
                    open("routes/resend_email_scripts/templates/promotional.jpg", "rb"),
                ),
            ],
            data={
                "from": "Regalia'22 Team <no-reply-regaila-pass@"
                + env_config.mailgun_domain
                + ">",
                "to": [mail],
                "subject": "Invitation for Regalia'22",
                "html": html_obj,
            },
        )

        print(f"{t.reason} - {t.status_code}")

    except Exception as e:
        print(e)
