# UserProxyGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**username** | **str** |  | 
**email** | **str** |  | 
**active** | **bool** |  | 
**edx_data** | **object** |  | 
**data** | **object** |  | 

## Example

```python
from iblai.models.user_proxy_get_response import UserProxyGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserProxyGetResponse from a JSON string
user_proxy_get_response_instance = UserProxyGetResponse.from_json(json)
# print the JSON string representation of the object
print(UserProxyGetResponse.to_json())

# convert the object into a dict
user_proxy_get_response_dict = user_proxy_get_response_instance.to_dict()
# create an instance of UserProxyGetResponse from a dict
user_proxy_get_response_from_dict = UserProxyGetResponse.from_dict(user_proxy_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


