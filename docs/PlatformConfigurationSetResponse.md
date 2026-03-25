# PlatformConfigurationSetResponse

Response serializer for setting platform configurations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** |  | [readonly] 
**results** | **List[Dict[str, object]]** | Results for each configuration item | [readonly] 
**total_set** | **int** | Total number of configurations set | [readonly] 

## Example

```python
from iblai.models.platform_configuration_set_response import PlatformConfigurationSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformConfigurationSetResponse from a JSON string
platform_configuration_set_response_instance = PlatformConfigurationSetResponse.from_json(json)
# print the JSON string representation of the object
print(PlatformConfigurationSetResponse.to_json())

# convert the object into a dict
platform_configuration_set_response_dict = platform_configuration_set_response_instance.to_dict()
# create an instance of PlatformConfigurationSetResponse from a dict
platform_configuration_set_response_from_dict = PlatformConfigurationSetResponse.from_dict(platform_configuration_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


