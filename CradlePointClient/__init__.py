import requests
import urllib3


class CradlePointError(Exception):
    pass


class CradlePointAuthError(Exception):
    pass


class Client:
    def __init__(self, verify=True, x_cp_api_id=None, x_cp_api_key=None, x_ecm_api_id=None, x_ecm_api_key=None):
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
            self.base_url = 'https://www.cradlepointecm.com/api/v2'
        else:
            raise AttributeError('The X-CP-API-ID, X-CP-API-KEY, X-ECM-API-ID and X-ECM-API-KEY are all required!')

    def get(self, method=str(), **kwargs):
        response = requests.get(f'{self.base_url}/{method.strip("/")}', headers=self.headers,
                                verify=self.verify, params=kwargs)
        if response.status_code in [200]:
            return response.json()
        else:
            raise CradlePointError(response.status_code)

    def add(self, method: str, data: dict) -> dict:
        response = requests.post(f'{self.base_url}/{method.strip("/")}', headers=self.headers,
                                 verify=self.verify, json=data)
        if response.status_code in [200]:
            return response.json()
        else:
            raise CradlePointError(response.status_code)

    def update(self, method: str, data: dict) -> dict:
        response = requests.put(f'{self.base_url}/{method.strip("/")}', headers=self.headers,
                                verify=self.verify, json=data)
        if response.status_code in [200]:
            return response.json()
        else:
            raise CradlePointError(response.status_code)

    def delete(self, method: str) -> dict:
        response = requests.delete(f'{self.base_url}/{method.strip("/")}', headers=self.headers, verify=self.verify)
        if response.status_code in [200]:
            return response.json()
        else:
            raise CradlePointError(response.status_code)
