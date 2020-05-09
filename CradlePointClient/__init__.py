import requests
import urllib3


class CradlePointError(Exception):
    pass


class CradlePointAuthError(Exception):
    pass


class APIClient:
    def __init__(self, verify=True, warnings=False, api_version='v2'):
        self.verify = bool(verify)
        self.api_version = api_version
        if warnings is False:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.headers = {'Content-Type': 'application/json'}
        self.token = None
        self.base_uri = None

    def connect(self, x_cp_api_id=None, x_cp_api_key=None, x_ecm_api_id=None, x_ecm_api_key=None):
        check_headers = {x_cp_api_id, x_cp_api_key, x_ecm_api_id, x_ecm_api_key}

        if None not in check_headers:
            headers = {
                'X-CP-API-ID': x_cp_api_id,
                'X-CP-API-KEY': x_cp_api_key,
                'X-ECM-API-ID': x_ecm_api_id,
                'X-ECM-API-KEY': x_ecm_api_key,
                'Content-Type': 'application/json'
            }

            self.headers = headers
            self.base_uri = f'https://www.cradlepointecm.com/api/{self.api_version}'
        else:
            raise AttributeError('The X-CP-API-ID, X-CP-API-KEY, X-ECM-API-ID and X-ECM-API-KEY are all required!')

    def disconnect(self):
        pass

    def get(self, url=None, method='', **kwargs):
        url = f'{self.base_uri}/{method.strip("/")}' if url is None else url
        return requests.get(url, headers=self.headers, verify=self.verify, params=kwargs)

    def post(self, url=None, method='', data=None):
        url = f'{self.base_uri}/{method.strip("/")}' if url is None else url
        return requests.post(url, headers=self.headers, verify=self.verify, json=data)

    def put(self, url=None, method='', data=None):
        url = f'{self.base_uri}/{method.strip("/")}' if url is None else url
        return requests.put(url, headers=self.headers, verify=self.verify, json=data)

    def delete(self, url=None, method=''):
        url = f'{self.base_uri}/{method.strip("/")}' if url is None else url
        return requests.delete(url, headers=self.headers, verify=self.verify)
