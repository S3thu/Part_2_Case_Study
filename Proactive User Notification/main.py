from linkedin_utils import login_to_linkedin, get_unread_messages_count, get_unread_notifications_count
from excel_utils import update_excel
from email_utils import send_email

# Define the LinkedIn usernames and encrypted passwords
user_credentials = [
    {"username": "user1", "encrypted_password": "password1"},
    {"username": "user2", "encrypted_password": "password2"},
    # Add more user credentials as needed
]

# Define the recipient email addresses
recipient_emails = [
    "recipient1@gmail.com",
    "recipient2@gmail.com",
    # Add more recipient emails as needed
]

# Perform the LinkedIn login and data retrieval for each user
for user in user_credentials:
    username = user["username"]
    encrypted_password = user["encrypted_password"]

    # Log in to LinkedIn
    driver = login_to_linkedin(username, encrypted_password)

    # Retrieve the number of unread messages and notifications
    messages_count = get_unread_messages_count(driver)
    notifications_count = get_unread_notifications_count(driver)

    # Close the WebDriver after retrieving data
    driver.quit()

    # Update the Excel file with the data
    file_path = "data.xlsx"  # Provide the path to the Excel file
    data = {"messages_count": messages_count,
            "notifications_count": notifications_count}
    update_excel(file_path, data)

# Send email notifications to each recipient
sender_email = "sender@gmail.com"  # Provide the sender's email address
# Provide the sender's email password (encrypted or secure)
sender_password = "sender_password"
subject = "LinkedIn Notifications"
for recipient_email in recipient_emails:
    # Compose the email body
    body = f"You have {messages_count} unread messages and {notifications_count} unread notifications on LinkedIn."

    # Send the email notification
    send_email(sender_email, sender_password, recipient_email, subject, body)
