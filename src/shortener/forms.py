from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(val):
    url_validator = URLValidator()
    try:
        url_validator(val)
    except:
        raise ValidationError("Invalid URL for this field")
    return val


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label="Submit URL", validators=[validate_url])

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     url = cleaned_data.get("url")
    #     print(url)

    def clean_url(self):
        url = self.cleaned_data["url"]
        if not ".com" in url:
            raise forms.ValidationError("This is not a valid URL because of no .com")
        # url_validator = URLValidator()
        # try:
        #     url_validator(url)
        # except:
        #     raise forms.ValidationError("Invalid URL for this field")
        # return url
