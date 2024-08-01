# TagsView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from iblai.models.tags_view import TagsView

# TODO update the JSON string below
json = "{}"
# create an instance of TagsView from a JSON string
tags_view_instance = TagsView.from_json(json)
# print the JSON string representation of the object
print(TagsView.to_json())

# convert the object into a dict
tags_view_dict = tags_view_instance.to_dict()
# create an instance of TagsView from a dict
tags_view_from_dict = TagsView.from_dict(tags_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


