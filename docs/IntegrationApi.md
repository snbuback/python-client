# wavefront_api_client.IntegrationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_integration**](IntegrationApi.md#get_all_integration) | **GET** /api/v2/integration | Gets a flat list of all Wavefront integrations available, along with their status
[**get_all_integration_0**](IntegrationApi.md#get_all_integration_0) | **GET** /api/v2/integration/installed | Gets a flat list of all Integrations that are installed, along with their status
[**get_all_integration_in_manifests**](IntegrationApi.md#get_all_integration_in_manifests) | **GET** /api/v2/integration/manifests | Gets all Wavefront integrations as structured in their integration manifests, along with their status
[**get_all_integration_statuses**](IntegrationApi.md#get_all_integration_statuses) | **GET** /api/v2/integration/status | Gets the status of all Wavefront integrations
[**get_integration**](IntegrationApi.md#get_integration) | **GET** /api/v2/integration/{id} | Gets a single Wavefront integration by its id, along with its status
[**get_integration_status**](IntegrationApi.md#get_integration_status) | **GET** /api/v2/integration/{id}/status | Gets the status of a single Wavefront integration
[**install_all_integration_alerts**](IntegrationApi.md#install_all_integration_alerts) | **POST** /api/v2/integration/{id}/install-all-alerts | Enable all alerts associated with this integration
[**install_integration**](IntegrationApi.md#install_integration) | **POST** /api/v2/integration/{id}/install | Installs a Wavefront integration
[**uninstall_all_integration_alerts**](IntegrationApi.md#uninstall_all_integration_alerts) | **POST** /api/v2/integration/{id}/uninstall-all-alerts | Disable all alerts associated with this integration
[**uninstall_integration**](IntegrationApi.md#uninstall_integration) | **POST** /api/v2/integration/{id}/uninstall | Uninstalls a Wavefront integration


# **get_all_integration**
> ResponseContainerPagedIntegration get_all_integration(offset=offset, limit=limit)

Gets a flat list of all Wavefront integrations available, along with their status



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.IntegrationApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Gets a flat list of all Wavefront integrations available, along with their status
    api_response = api_instance.get_all_integration(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_all_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedIntegration**](ResponseContainerPagedIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_integration_0**
> ResponseContainerListIntegration get_all_integration_0()

Gets a flat list of all Integrations that are installed, along with their status



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.IntegrationApi(wavefront_api_client.ApiClient(configuration))

try:
    # Gets a flat list of all Integrations that are installed, along with their status
    api_response = api_instance.get_all_integration_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_all_integration_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerListIntegration**](ResponseContainerListIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_integration_in_manifests**
> ResponseContainerListIntegrationManifestGroup get_all_integration_in_manifests()

Gets all Wavefront integrations as structured in their integration manifests, along with their status



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.IntegrationApi(wavefront_api_client.ApiClient(configuration))

try:
    # Gets all Wavefront integrations as structured in their integration manifests, along with their status
    api_response = api_instance.get_all_integration_in_manifests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_all_integration_in_manifests: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerListIntegrationManifestGroup**](ResponseContainerListIntegrationManifestGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_integration_statuses**
> ResponseContainerMapStringIntegrationStatus get_all_integration_statuses()

Gets the status of all Wavefront integrations



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.IntegrationApi(wavefront_api_client.ApiClient(configuration))

try:
    # Gets the status of all Wavefront integrations
    api_response = api_instance.get_all_integration_statuses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_all_integration_statuses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerMapStringIntegrationStatus**](ResponseContainerMapStringIntegrationStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration**
> ResponseContainerIntegration get_integration(id, refresh=refresh)

Gets a single Wavefront integration by its id, along with its status



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.IntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
refresh = true # bool |  (optional)

try:
    # Gets a single Wavefront integration by its id, along with its status
    api_response = api_instance.get_integration(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **refresh** | **bool**|  | [optional] 

### Return type

[**ResponseContainerIntegration**](ResponseContainerIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_status**
> ResponseContainerIntegrationStatus get_integration_status(id)

Gets the status of a single Wavefront integration



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.IntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Gets the status of a single Wavefront integration
    api_response = api_instance.get_integration_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->get_integration_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerIntegrationStatus**](ResponseContainerIntegrationStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_all_integration_alerts**
> ResponseContainerIntegrationStatus install_all_integration_alerts(id, body=body)

Enable all alerts associated with this integration



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.IntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.InstallAlerts() # InstallAlerts |  (optional)

try:
    # Enable all alerts associated with this integration
    api_response = api_instance.install_all_integration_alerts(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->install_all_integration_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**InstallAlerts**](InstallAlerts.md)|  | [optional] 

### Return type

[**ResponseContainerIntegrationStatus**](ResponseContainerIntegrationStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_integration**
> ResponseContainerIntegrationStatus install_integration(id)

Installs a Wavefront integration



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.IntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Installs a Wavefront integration
    api_response = api_instance.install_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->install_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerIntegrationStatus**](ResponseContainerIntegrationStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall_all_integration_alerts**
> ResponseContainerIntegrationStatus uninstall_all_integration_alerts(id)

Disable all alerts associated with this integration



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.IntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Disable all alerts associated with this integration
    api_response = api_instance.uninstall_all_integration_alerts(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->uninstall_all_integration_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerIntegrationStatus**](ResponseContainerIntegrationStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall_integration**
> ResponseContainerIntegrationStatus uninstall_integration(id)

Uninstalls a Wavefront integration



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.IntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Uninstalls a Wavefront integration
    api_response = api_instance.uninstall_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->uninstall_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerIntegrationStatus**](ResponseContainerIntegrationStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

