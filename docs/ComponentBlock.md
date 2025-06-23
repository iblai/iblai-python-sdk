# ComponentBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**unit** | **int** |  | 
**type** | [**ComponentBlockTypeEnum**](ComponentBlockTypeEnum.md) |  | [optional] 
**display_name** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.component_block import ComponentBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentBlock from a JSON string
component_block_instance = ComponentBlock.from_json(json)
# print the JSON string representation of the object
print(ComponentBlock.to_json())

# convert the object into a dict
component_block_dict = component_block_instance.to_dict()
# create an instance of ComponentBlock from a dict
component_block_from_dict = ComponentBlock.from_dict(component_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


