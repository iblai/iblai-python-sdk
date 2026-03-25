# ConfigurationItem

Serializer for individual configuration items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Configuration key | 
**value** | **object** | Configuration value stored as JSON | 

## Example

```python
from iblai.models.configuration_item import ConfigurationItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationItem from a JSON string
configuration_item_instance = ConfigurationItem.from_json(json)
# print the JSON string representation of the object
print(ConfigurationItem.to_json())

# convert the object into a dict
configuration_item_dict = configuration_item_instance.to_dict()
# create an instance of ConfigurationItem from a dict
configuration_item_from_dict = ConfigurationItem.from_dict(configuration_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


