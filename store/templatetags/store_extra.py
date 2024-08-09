from django import template
from urllib.parse import urlparse, urlencode, parse_qsl

def update_path_page(url, arg):
    url_parts = urlparse(url)
    query = dict(parse_qsl(url_parts.query))
    query['page'] = arg
    query.update(query)

    new_url = url_parts._replace(query=urlencode(query)).geturl()

    return new_url


register = template.Library()
register.filter("update_path_page", update_path_page)
