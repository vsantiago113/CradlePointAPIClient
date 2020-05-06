import requests
import urllib3


class CradlePointError(Exception):
    pass


class CradlePointAuthError(Exception):
    pass


class Client:
    def __init__(self, verify=True, api_version='v2', x_cp_api_id=None, x_cp_api_key=None, 
                 x_ecm_api_id=None, x_ecm_api_key=None):
        self.verify = bool(verify)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
            self.base_url = f'https://www.cradlepointecm.com/api/{api_version}'
        else:
            raise AttributeError('The X-CP-API-ID, X-CP-API-KEY, X-ECM-API-ID and X-ECM-API-KEY are all required!')

    def get(self, url=None, method='', **kwargs):
        url = f'{self.base_url}/{method.strip("/")}' if url is None else url
        response = requests.get(url, headers=self.headers, verify=self.verify, params=kwargs)
        if response.status_code in [200, 202]:
            return response.json()
        else:
            raise CradlePointError(response.status_code)

    def add(self, url=None, method='', data=None) -> dict:
        url = f'{self.base_url}/{method.strip("/")}' if url is None else url
        response = requests.post(url, headers=self.headers, verify=self.verify, json=data)
        if response.status_code in [200, 202]:
            return response.json()
        else:
            raise CradlePointError(response.status_code)

    def update(self, url=None, method='', data=None) -> dict:
        url = f'{self.base_url}/{method.strip("/")}' if url is None else url
        response = requests.put(url, headers=self.headers, verify=self.verify, json=data)
        if response.status_code in [200, 202]:
            return response.json()
        else:
            raise CradlePointError(response.status_code)

    def delete(self, url=None, method='') -> dict:
        url = f'{self.base_url}/{method.strip("/")}' if url is None else url
        response = requests.delete(url, headers=self.headers, verify=self.verify)
        if response.status_code in [200, 202]:
            return response.json()
        else:
            raise CradlePointError(response.status_code)
