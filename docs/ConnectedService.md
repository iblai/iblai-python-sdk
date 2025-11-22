# ConnectedService

Serializer for representing connected OAuth services.  Includes both the legacy `service` / `scope` string values and structured representations so that consumers can reason about individual scope names.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**provider** | **str** |  | 
**service** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**scope** | **str** |  | [optional] 
**scope_names** | **List[str]** | Return the canonical list of scope identifiers for the connection. | [readonly] 
**scopes** | **List[str]** | Return the OAuth scope strings associated with the connection. | [readonly] 
**token_type** | **str** |  | [optional] 
**service_info** | [**ExternalServiceInfo**](ExternalServiceInfo.md) |  | [readonly] 

## Example

```python
from iblai.models.connected_service import ConnectedService

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedService from a JSON string
connected_service_instance = ConnectedService.from_json(json)
# print the JSON string representation of the object
print(ConnectedService.to_json())

# convert the object into a dict
connected_service_dict = connected_service_instance.to_dict()
# create an instance of ConnectedService from a dict
connected_service_from_dict = ConnectedService.from_dict(connected_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


