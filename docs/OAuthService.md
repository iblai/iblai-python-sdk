# OAuthService

Read-only serializer exposing details about an OAuth service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**oauth_provider** | **str** |  | [readonly] 
**oauth_provider_id** | **int** |  | [optional] 
**name** | **str** |  | [readonly] 
**display_name** | **str** | Human readable label for the OAuth service scope. | [readonly] 
**description** | **str** |  | [readonly] 
**scope** | **str** |  | [readonly] 
**image** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.o_auth_service import OAuthService

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthService from a JSON string
o_auth_service_instance = OAuthService.from_json(json)
# print the JSON string representation of the object
print(OAuthService.to_json())

# convert the object into a dict
o_auth_service_dict = o_auth_service_instance.to_dict()
# create an instance of OAuthService from a dict
o_auth_service_from_dict = OAuthService.from_dict(o_auth_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


