# wavefront_api_client.UserApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_user_groups**](UserApi.md#add_user_to_user_groups) | **POST** /api/v2/user/{id}/addUserGroups | Adds specific user groups to the user
[**create_or_update_user**](UserApi.md#create_or_update_user) | **POST** /api/v2/user | Creates or updates a user
[**delete_multiple_users**](UserApi.md#delete_multiple_users) | **POST** /api/v2/user/deleteUsers | Deletes multiple users
[**delete_user**](UserApi.md#delete_user) | **DELETE** /api/v2/user/{id} | Deletes a user identified by id
[**get_all_user**](UserApi.md#get_all_user) | **GET** /api/v2/user | Get all users
[**get_user**](UserApi.md#get_user) | **GET** /api/v2/user/{id} | Retrieves a user by identifier (email addr)
[**grant_permission_to_users**](UserApi.md#grant_permission_to_users) | **POST** /api/v2/user/grant/{permission} | Grants a specific user permission to multiple users
[**grant_user_permission**](UserApi.md#grant_user_permission) | **POST** /api/v2/user/{id}/grant | Grants a specific user permission
[**invite_users**](UserApi.md#invite_users) | **POST** /api/v2/user/invite | Invite users with given user groups and permissions.
[**remove_user_from_user_groups**](UserApi.md#remove_user_from_user_groups) | **POST** /api/v2/user/{id}/removeUserGroups | Removes specific user groups from the user
[**revoke_permission_from_users**](UserApi.md#revoke_permission_from_users) | **POST** /api/v2/user/revoke/{permission} | Revokes a specific user permission from multiple users
[**revoke_user_permission**](UserApi.md#revoke_user_permission) | **POST** /api/v2/user/{id}/revoke | Revokes a specific user permission
[**update_user**](UserApi.md#update_user) | **PUT** /api/v2/user/{id} | Update user with given user groups and permissions.


# **add_user_to_user_groups**
> UserModel add_user_to_user_groups(id, body=body)

Adds specific user groups to the user



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] | The list of user groups that should be added to the user (optional)

try:
    # Adds specific user groups to the user
    api_response = api_instance.add_user_to_user_groups(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add_user_to_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| The list of user groups that should be added to the user | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_user**
> UserModel create_or_update_user(send_email=send_email, body=body)

Creates or updates a user



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
send_email = true # bool | Whether to send email notification to the user, if created.  Default: false (optional)
body = wavefront_api_client.UserToCreate() # UserToCreate | Example Body:  <pre>{   \"emailAddress\": \"user@example.com\",   \"groups\": [     \"user_management\"   ],   \"userGroups\": [     \"8b23136b-ecd2-4cb5-8c92-62477dcc4090\"   ] }</pre> (optional)

try:
    # Creates or updates a user
    api_response = api_instance.create_or_update_user(send_email=send_email, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_or_update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_email** | **bool**| Whether to send email notification to the user, if created.  Default: false | [optional] 
 **body** | [**UserToCreate**](UserToCreate.md)| Example Body:  &lt;pre&gt;{   \&quot;emailAddress\&quot;: \&quot;user@example.com\&quot;,   \&quot;groups\&quot;: [     \&quot;user_management\&quot;   ],   \&quot;userGroups\&quot;: [     \&quot;8b23136b-ecd2-4cb5-8c92-62477dcc4090\&quot;   ] }&lt;/pre&gt; | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_multiple_users**
> ResponseContainerListString delete_multiple_users(body=body)

Deletes multiple users



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.list[str]()] # list[str] | identifiers of list of users which should be deleted (optional)

try:
    # Deletes multiple users
    api_response = api_instance.delete_multiple_users(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_multiple_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| identifiers of list of users which should be deleted | [optional] 

### Return type

[**ResponseContainerListString**](ResponseContainerListString.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(id)

Deletes a user identified by id



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Deletes a user identified by id
    api_instance.delete_user(id)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user**
> list[UserModel] get_all_user()

Get all users

Returns all users

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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get all users
    api_response = api_instance.get_all_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_all_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserModel]**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserModel get_user(id)

Retrieves a user by identifier (email addr)



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Retrieves a user by identifier (email addr)
    api_response = api_instance.get_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_permission_to_users**
> UserModel grant_permission_to_users(permission, body=body)

Grants a specific user permission to multiple users



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
permission = 'permission_example' # str | Permission to grant to the users. Please note that 'host_tag_management' is the equivalent of the 'Source Tag Management' permission
body = [wavefront_api_client.list[str]()] # list[str] | list of users which should be revoked by specified permission (optional)

try:
    # Grants a specific user permission to multiple users
    api_response = api_instance.grant_permission_to_users(permission, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->grant_permission_to_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| Permission to grant to the users. Please note that &#39;host_tag_management&#39; is the equivalent of the &#39;Source Tag Management&#39; permission | 
 **body** | **list[str]**| list of users which should be revoked by specified permission | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_user_permission**
> UserModel grant_user_permission(id, group=group)

Grants a specific user permission



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
group = 'group_example' # str | Permission group to grant to this user.  Please note that 'host_tag_management' is the equivalent of the 'Source Tag Management' permission (optional)

try:
    # Grants a specific user permission
    api_response = api_instance.grant_user_permission(id, group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->grant_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **group** | **str**| Permission group to grant to this user.  Please note that &#39;host_tag_management&#39; is the equivalent of the &#39;Source Tag Management&#39; permission | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_users**
> UserModel invite_users(body=body)

Invite users with given user groups and permissions.



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.UserToCreate()] # list[UserToCreate] | Example Body:  <pre>[ {   \"emailAddress\": \"user@example.com\",   \"groups\": [     \"user_management\"   ],   \"userGroups\": [     \"8b23136b-ecd2-4cb5-8c92-62477dcc4090\"   ] } ]</pre> (optional)

try:
    # Invite users with given user groups and permissions.
    api_response = api_instance.invite_users(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->invite_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UserToCreate]**](UserToCreate.md)| Example Body:  &lt;pre&gt;[ {   \&quot;emailAddress\&quot;: \&quot;user@example.com\&quot;,   \&quot;groups\&quot;: [     \&quot;user_management\&quot;   ],   \&quot;userGroups\&quot;: [     \&quot;8b23136b-ecd2-4cb5-8c92-62477dcc4090\&quot;   ] } ]&lt;/pre&gt; | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_user_groups**
> UserModel remove_user_from_user_groups(id, body=body)

Removes specific user groups from the user



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] | The list of user groups that should be removed from the user (optional)

try:
    # Removes specific user groups from the user
    api_response = api_instance.remove_user_from_user_groups(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->remove_user_from_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| The list of user groups that should be removed from the user | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_permission_from_users**
> UserModel revoke_permission_from_users(permission, body=body)

Revokes a specific user permission from multiple users



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
permission = 'permission_example' # str | Permission to grant to the users. Please note that 'host_tag_management' is the equivalent of the 'Source Tag Management' permission
body = [wavefront_api_client.list[str]()] # list[str] | list of users which should be revoked by specified permission (optional)

try:
    # Revokes a specific user permission from multiple users
    api_response = api_instance.revoke_permission_from_users(permission, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->revoke_permission_from_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| Permission to grant to the users. Please note that &#39;host_tag_management&#39; is the equivalent of the &#39;Source Tag Management&#39; permission | 
 **body** | **list[str]**| list of users which should be revoked by specified permission | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_user_permission**
> UserModel revoke_user_permission(id, group=group)

Revokes a specific user permission



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
group = 'group_example' # str |  (optional)

try:
    # Revokes a specific user permission
    api_response = api_instance.revoke_user_permission(id, group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->revoke_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **group** | **str**|  | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserModel update_user(id, body=body)

Update user with given user groups and permissions.



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.UserRequestDTO() # UserRequestDTO | Example Body:  <pre>{   \"identifier\": \"user@example.com\",   \"groups\": [     \"user_management\"   ],   \"userGroups\": [     \"8b23136b-ecd2-4cb5-8c92-62477dcc4090\"   ] }</pre> (optional)

try:
    # Update user with given user groups and permissions.
    api_response = api_instance.update_user(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**UserRequestDTO**](UserRequestDTO.md)| Example Body:  &lt;pre&gt;{   \&quot;identifier\&quot;: \&quot;user@example.com\&quot;,   \&quot;groups\&quot;: [     \&quot;user_management\&quot;   ],   \&quot;userGroups\&quot;: [     \&quot;8b23136b-ecd2-4cb5-8c92-62477dcc4090\&quot;   ] }&lt;/pre&gt; | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

