from decouple import config
from flask import request, url_for, redirect


def validate_headers(headers):
    content_type = headers.get('Content-Type')
    if content_type != 'application/json':
        return redirect(url_for(config('DEFAULT_BLUEPRINT')))

    return True
