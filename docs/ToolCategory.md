# ToolCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from iblai.models.tool_category import ToolCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCategory from a JSON string
tool_category_instance = ToolCategory.from_json(json)
# print the JSON string representation of the object
print(ToolCategory.to_json())

# convert the object into a dict
tool_category_dict = tool_category_instance.to_dict()
# create an instance of ToolCategory from a dict
tool_category_from_dict = ToolCategory.from_dict(tool_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


