import logging

from django.views import View

from django.shortcuts import render
from pir_frontend.forms import PIRForm

logger = logging.getLogger(__name__)


class PIRView(View):
    def post(self, request):
        form = PIRForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            try:
                form.client.create_report(data)
            except Exception as e:
                logger.exception('Failed to use service')
                return render(
                    request, 'index.html', {
                        'error': (
                            'Something is wrong with the service.'
                            ' Please try again later'
                        )
                    },
                    status=500
                )

            return render(
                request, 'index.html', {'email': data['email']},
                status=201
            )
        else:
            return render(
                request, 'index.html', {'form': form},
                status=400
            )

    def get(self, request):
        return render(
            request, 'index.html', {'form': PIRForm()},
        )
