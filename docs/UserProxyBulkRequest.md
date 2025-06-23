# UserProxyBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[Dict[str, str]]** |  | 

## Example

```python
from iblai.models.user_proxy_bulk_request import UserProxyBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserProxyBulkRequest from a JSON string
user_proxy_bulk_request_instance = UserProxyBulkRequest.from_json(json)
# print the JSON string representation of the object
print(UserProxyBulkRequest.to_json())

# convert the object into a dict
user_proxy_bulk_request_dict = user_proxy_bulk_request_instance.to_dict()
# create an instance of UserProxyBulkRequest from a dict
user_proxy_bulk_request_from_dict = UserProxyBulkRequest.from_dict(user_proxy_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


