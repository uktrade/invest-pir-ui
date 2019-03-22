import logging
import boto3

from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.conf import settings

from pir_frontend.forms import PIRForm
from botocore.errorfactory import ClientError
from directory_components.mixins import CountryDisplayMixin

logger = logging.getLogger(__name__)


class PIRView(CountryDisplayMixin, View):
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


class ProxyView(CountryDisplayMixin, View):
    def get(self, request, filename):
        client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_S3_PDF_STORE_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_S3_PDF_STORE_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_PDF_STORE_BUCKET_REGION,
        )

        try:
            client.head_object(
                Bucket=settings.AWS_S3_PDF_STORE_BUCKET_NAME, Key=filename
            )
        except ClientError:
            raise Http404

        url = client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': settings.AWS_S3_PDF_STORE_BUCKET_NAME,
                'Key': filename
            },
            ExpiresIn=3600
        )

        return HttpResponseRedirect(url)
