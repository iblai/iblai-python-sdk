# PlatformConfigurationSet

Serializer for setting platform configurations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | Platform key to set configurations for | 
**configurations** | [**List[ConfigurationItem]**](ConfigurationItem.md) | List of configurations to set | 

## Example

```python
from iblai.models.platform_configuration_set import PlatformConfigurationSet

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformConfigurationSet from a JSON string
platform_configuration_set_instance = PlatformConfigurationSet.from_json(json)
# print the JSON string representation of the object
print(PlatformConfigurationSet.to_json())

# convert the object into a dict
platform_configuration_set_dict = platform_configuration_set_instance.to_dict()
# create an instance of PlatformConfigurationSet from a dict
platform_configuration_set_from_dict = PlatformConfigurationSet.from_dict(platform_configuration_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


