from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(val):
    url_validator = URLValidator()
    value_1_invalid = False
    value_2_invalid = False
    try:
        url_validator(val)
    except:
        value_1_invalid = True
    value_2_url = "http://" + val
    try:
        url_validator(value_2_url)
    except:
        value_2_invalid = True

    if value_1_invalid == True and value_2_invalid == True:
        raise ValidationError("Invalid URL for this field")
    return val


def validate_dot_com(val):
    if not ".com" in val:
        raise ValidationError("This is not a valid URL because of no .com")
    return val
