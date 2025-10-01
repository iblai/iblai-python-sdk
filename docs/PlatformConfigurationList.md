# PlatformConfigurationList

Serializer for listing platform configurations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** |  | [readonly] 
**configurations** | **Dict[str, object]** | Dictionary of configuration key-value pairs with proper type casting | [readonly] 
**count** | **int** | Number of configurations returned | [readonly] 

## Example

```python
from iblai.models.platform_configuration_list import PlatformConfigurationList

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformConfigurationList from a JSON string
platform_configuration_list_instance = PlatformConfigurationList.from_json(json)
# print the JSON string representation of the object
print(PlatformConfigurationList.to_json())

# convert the object into a dict
platform_configuration_list_dict = platform_configuration_list_instance.to_dict()
# create an instance of PlatformConfigurationList from a dict
platform_configuration_list_from_dict = PlatformConfigurationList.from_dict(platform_configuration_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


