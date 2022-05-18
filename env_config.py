"""
loads env secrets
"""

import os
import dotenv

dotenv.load_dotenv()
username = os.getenv("ADMIN_USERNAME")
password = os.getenv("PASSWORD")
cluster_name = os.getenv("CLUSTER_NAME")
database = os.getenv("DATABASE")
token_key = os.getenv("TOKEN_KEY")
mailgun_key = os.getenv("MAILGUN_KEY")
token = os.getenv("TOKEN")
mailgun_domain = os.getenv("MAILGUN_DOMAIN")
create_pass_api = os.getenv("CREATE_PASS_API")
