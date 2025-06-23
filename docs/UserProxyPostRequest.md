# UserProxyPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**username** | **str** |  | 
**email** | **str** |  | 
**edx_data** | **object** |  | 
**data** | **object** |  | 

## Example

```python
from iblai.models.user_proxy_post_request import UserProxyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserProxyPostRequest from a JSON string
user_proxy_post_request_instance = UserProxyPostRequest.from_json(json)
# print the JSON string representation of the object
print(UserProxyPostRequest.to_json())

# convert the object into a dict
user_proxy_post_request_dict = user_proxy_post_request_instance.to_dict()
# create an instance of UserProxyPostRequest from a dict
user_proxy_post_request_from_dict = UserProxyPostRequest.from_dict(user_proxy_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


