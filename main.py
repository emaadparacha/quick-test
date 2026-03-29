import os
import random
from datetime import datetime, timezone

from twilio.rest import Client


def main():
    # Code Engine gives each parallel job instance an index via JOB_INDEX
    job_index = os.getenv("JOB_INDEX", "0")

    # Random number just for fun / uniqueness
    random_number = random.randint(1000, 9999)

    # Current time in ISO 8601 (UTC)
    now_utc = datetime.now(timezone.utc).isoformat()

    # Twilio credentials & numbers from environment variables
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    from_number = os.environ["TWILIO_FROM_NUMBER"]  # your Twilio number
    to_number = os.environ["TO_NUMBER"]             # your phone number


    client = Client(account_sid, auth_token)

    body = (
        f"IBM Cloud Code Engine demo:\n"
        f"This is worker {job_index} - {random_number}\n"
        f"Time (UTC): {now_utc}"
    )

    message = client.messages.create(
        body=body,
        from_=from_number,
        to=to_number,
    )

    # Log something so you can see it in job run logs
    print(f"Sent SMS from worker {job_index} - {random_number}, SID={message.sid}")


if __name__ == "__main__":
    main()
