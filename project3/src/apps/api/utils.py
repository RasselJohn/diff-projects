def get_form_errors(form):
    errors_list = [''.join(e) for e in form.errors.values()]
    return {'status': ";".join(errors_list)}


def get_base_domain(url):
    # Standard python urlparse package does not work correctly.
    if not url or '.' not in url:
        return None

    base_url = url.lower()

    # remove protocol
    if '://' in base_url:
        base_url = base_url.split("://")[1]

    # remove part after domain and query params
    base_url = base_url.split('/')[0].split("?")[0]

    return base_url
