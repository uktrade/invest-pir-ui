import logging

from requests.exceptions import HTTPError
from django.shortcuts import render
from pir_frontend.forms import PIRForm

logger = logging.getLogger(__name__)

# Create your views here.
def form_base(request):
    form = PIRForm()
    context = {}

    if request.method == 'POST':
        form = PIRForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            try:
                form.client.create_report(data)
            except Exception as e:
                logger.exception('Failed to use service')
                return render(request, 'index.html',{
                    'error': (
                        'Something is wrong with the service.'
                        ' Please try again later'
                    )
                })

            return render(request, 'index.html', {
                'email': data['email']
            })

    return render(request, 'index.html', {
        'form': form
    })
