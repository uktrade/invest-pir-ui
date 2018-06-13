from django.conf import settings

from directory_components import forms, fields
from django_countries.data import COUNTRIES

from pir_client import PIRAPIClient


class PIRForm(forms.Form):
    name = fields.CharField(
        required=True,
        label='Name',
        help_text='Name'
    )
    company = fields.CharField(
        required=True,
        label='Company',
        help_text='Company'
    )

    email = fields.EmailField(
        required=True,
        label='Email',
        help_text='Email'
    )

    country = fields.ChoiceField(
        required=True,
        label='Country',
        help_text='Country',
        choices=[
            (k, v) for k, v in COUNTRIES.items()
        ]
    )


    def __init__(self, *args, **kwargs):
        super(PIRForm, self).__init__(*args, **kwargs)
        self.client = PIRAPIClient(
            base_url=settings.PIR_API_URL,
            api_key=settings.PIR_API_KEY
        )

        options = self.client.get_options()

        sector_choices = [
            (o['value'], o['display_name']) for o in options['sector']['choices']
        ]

        self.fields['sector'] = fields.ChoiceField(
            label='Sector',
            help_text='Sector',
            choices=sector_choices
        )
