import requests


_configs = {}


def fetch_openid_config(issuer):
    global _configs

    if issuer not in _configs:
        resp = requests.get(issuer.rstrip("/") + "/.well-known/openid-configuration", timeout=60)
        _configs[issuer] = resp.json()

    return _configs[issuer]
