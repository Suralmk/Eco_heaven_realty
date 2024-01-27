from django.core.mail import send_mail


def send_password_reset_email(email, token):

    email_send = send_mail(
        "password reset request",
        f"Use this url to reset your password http://127.0.0.1:8000/create-password/{token}/",
        "surafelmelaku940@gmail.com",
        [f"{email}"],
        fail_silently=True

    )

    if email_send : return True 
    else: return False 

