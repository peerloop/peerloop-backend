from email_validator import EmailNotValidError, validate_email

from peerloop.core.exceptions.validation import InvalidEmailError


def validate_email_format(email: str) -> str:
    try:
        validation = validate_email(email)
        valid_email = validation.email
    except EmailNotValidError:
        raise InvalidEmailError(f"Invalid Email Error: {email} is not a valid email address.")
    return valid_email
