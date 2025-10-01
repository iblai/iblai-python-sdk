# ExternalServiceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**display_name** | **str** |  | 
**logo** | **str** |  | [optional] 

## Example

```python
from iblai.models.external_service_info import ExternalServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalServiceInfo from a JSON string
external_service_info_instance = ExternalServiceInfo.from_json(json)
# print the JSON string representation of the object
print(ExternalServiceInfo.to_json())

# convert the object into a dict
external_service_info_dict = external_service_info_instance.to_dict()
# create an instance of ExternalServiceInfo from a dict
external_service_info_from_dict = ExternalServiceInfo.from_dict(external_service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


