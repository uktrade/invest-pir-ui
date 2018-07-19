from django.test import TestCase
from unittest.mock import patch

OPTIONS_DATA = {
    "country": {
        "choices": [
            {
                "value": "AF",
                "display_name": "Afghanistan"
            },
        ]
    },
    "market": {
        "choices": [
            {
                "value": "africa",
                "display_name": "africa"
            },
            {
                "value": "canada",
                "display_name": "canada"
            }
        ]
    },
    "sector": {
        "choices": [
            {
                "value": "tech",
                "display_name": "Technology"
            },
            {
                "value": "automotive",
                "display_name": "Automotive"
            },
        ]
    }
}


class ViewTest(TestCase):

    @patch('pir_frontend.forms.PIRAPIClient')
    def test_pir_view(self, client_instance_mock):
        client_instance_mock().get_options.return_value = OPTIONS_DATA

        valid_data = {
            'name': 'Ted',
            'company': 'Corp',
            'email': 'ted@example.com',
            'country': 'US',
            'sector': 'tech',
            'g-recaptcha-response': 'PASSED',
            'check': 'on'
        }

        res = self.client.get('/')
        self.assertEquals(res.status_code, 200)

        res = self.client.post('/', data=valid_data)
        self.assertEquals(res.status_code, 201)

        res = self.client.post('/', data={'name': 'Ted', })
        self.assertEquals(res.status_code, 400)

        client_instance_mock().create_report.side_effect = ValueError()
        res = self.client.post('/', data=valid_data)
        self.assertEquals(res.status_code, 500)
