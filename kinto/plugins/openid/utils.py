from security import safe_requests


_configs = {}


def fetch_openid_config(issuer):
    global _configs

    if issuer not in _configs:
        resp = safe_requests.get(issuer.rstrip("/") + "/.well-known/openid-configuration")
        _configs[issuer] = resp.json()

    return _configs[issuer]
