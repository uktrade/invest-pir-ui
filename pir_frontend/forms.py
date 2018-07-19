from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from directory_components import forms, fields
from django_countries.data import COUNTRIES
from nocaptcha_recaptcha.fields import NoReCaptchaField

from pir_client.client import PIRAPIClient


class PIRForm(forms.Form):
    name = fields.CharField(
        required=True,
        label=_('Name'),
    )
    company = fields.CharField(
        required=True,
        label=_('Company'),
    )

    email = fields.EmailField(
        required=True,
        label=_('Email'),
    )

    country = fields.ChoiceField(
        required=True,
        label=_('Country'),
        choices=sorted(
            [(k, v) for k, v in COUNTRIES.items()],
            key=lambda tup: tup[1]
        )
    )

    def __init__(self, *args, **kwargs):
        super(PIRForm, self).__init__(*args, **kwargs)
        self.client = PIRAPIClient(
            base_url=settings.PIR_API_URL,
            api_key=settings.PIR_API_KEY
        )

        options = self.client.get_options()

        sector_choices = [
            (
                o['value'],
                o['display_name']) for o in options['sector']['choices']
        ]

        self.fields['sector'] = fields.ChoiceField(
            label='Sector',
            choices=sector_choices
        )

        self.fields['captcha'] = NoReCaptchaField()
