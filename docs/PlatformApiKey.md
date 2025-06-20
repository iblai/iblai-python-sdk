# PlatformApiKey

Serializer for PlatformApiKey's

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username that created token | [readonly] 
**name** | **str** | Name of the token. Used by the user to identify the token. | 
**key** | **str** |  | [readonly] 
**platform_key** | **str** | The platform key | 
**expires** | **datetime** | When token expires | [readonly] 
**expires_in** | **str** | Optional duration until key expires. Format: [DD] [HH:[MM:]]ss[.uuuuuu] | [optional] 
**created** | **datetime** | When token was created | [readonly] 

## Example

```python
from iblai.models.platform_api_key import PlatformApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformApiKey from a JSON string
platform_api_key_instance = PlatformApiKey.from_json(json)
# print the JSON string representation of the object
print(PlatformApiKey.to_json())

# convert the object into a dict
platform_api_key_dict = platform_api_key_instance.to_dict()
# create an instance of PlatformApiKey from a dict
platform_api_key_from_dict = PlatformApiKey.from_dict(platform_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


