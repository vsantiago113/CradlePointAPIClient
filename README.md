# CradlepointAPIClient
[NetCloud API](https://developer.cradlepoint.com/ "NetCloud API")

---

![PyPI - Status](https://img.shields.io/pypi/status/CradlepointAPIClient)
![PyPI - Format](https://img.shields.io/pypi/format/CradlepointAPIClient)
![GitHub](https://img.shields.io/github/license/vsantiago113/CradlepointAPIClient)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/vsantiago113/CradlepointAPIClient)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/CradlepointAPIClient)

An API Client for Cradlepoint to be able to easily use the API in a more standard way.

## How to install
```ignorelang
$ pip install CradlepointAPIClient
```

## Usage
the argument "method" must be specify every time. Look at authentication validation for an example.

#### Default arguments and attributes
```python
import CradlepointAPIClient

client = CradlepointAPIClient.Client(verify=False, warnings=False, api_version='v1')

client.get(url=None, method='', data=None, auth = None)

# client.headers
# client.url_base
# client.token

```

#### The first query
```python
import CradlepointAPIClient
import json

client = CradlepointAPIClient.Client()
client.connect(url='https://Cradlepoint-server.local', username='admin', password='Admin123')

response = client.get(method='/data/Alarms.json')
print(json.dumps(response.json(), indent=4))

client.disconnect()
```

#### Getting detailed information
```python
import CradlepointAPIClient
import json

client = CradlepointAPIClient.Client()
client.connect(url='https://Cradlepoint-server.local', username='admin', password='Admin123')

query_string = {'.full': 'true'}
response = client.get(method='/data/Alarms.json', **query_string)
print(json.dumps(response.json(), indent=4))

client.disconnect()
```

#### Sorting
```python
import CradlepointAPIClient
import json

client = CradlepointAPIClient.Client()
client.connect(url='https://Cradlepoint-server.local', username='admin', password='Admin123')

query_string = {'.full': 'true', '.sort': 'severity'}
response = client.get(method='/data/Alarms.json', **query_string)
print(json.dumps(response.json(), indent=4))

client.disconnect()
```

#### Filtering
```python
import CradlepointAPIClient
import json

client = CradlepointAPIClient.Client()
client.connect(url='https://Cradlepoint-server.local', username='admin', password='Admin123')

query_string = {'.full': 'true', '.sort': 'severity', 'category.value': 'AP',
                    'message': 'contains("interface")'}
response = client.get(method='/data/Alarms.json', **query_string)
print(json.dumps(response.json(), indent=4))

client.disconnect()
```

#### Paging
```python
import CradlepointAPIClient
import json

client = CradlepointAPIClient.Client()
client.connect(url='https://Cradlepoint-server.local', username='admin', password='Admin123')

query_string = {'.full': 'true', '.sort': 'severity', 'category.value': 'AP',
                    'message': 'contains("interface")', '.maxResults': '5'}
response = client.get(method='/data/Alarms.json', **query_string)
print(json.dumps(response.json(), indent=4))

client.disconnect()
```
