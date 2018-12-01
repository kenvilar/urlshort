from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(val):
    url_validator = URLValidator()
    reg_val = val
    if "http" in reg_val:
        new_value = reg_val
    else:
        new_value = "http://" + reg_val

    try:
        url_validator(new_value)
    except:
        raise ValidationError("Invalid URL for this field")
    return new_value


def validate_dot_com(val):
    if not ".com" in val:
        raise ValidationError("This is not a valid URL because of no .com")
    return val
