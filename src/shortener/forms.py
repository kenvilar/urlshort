from django import forms

from .validators import validate_dot_com, validate_url


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label="Submit URL", validators=[validate_url, validate_dot_com])

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     url = cleaned_data.get("url")
    #     print(url)

    # def clean_url(self):
    #     url = self.cleaned_data["url"]
    #     if not ".com" in url:
    #         raise forms.ValidationError("This is not a valid URL because of no .com")
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL for this field")
    #     return url
