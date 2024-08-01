# StylesView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**description** | **str** |  | 

## Example

```python
from iblai.models.styles_view import StylesView

# TODO update the JSON string below
json = "{}"
# create an instance of StylesView from a JSON string
styles_view_instance = StylesView.from_json(json)
# print the JSON string representation of the object
print(StylesView.to_json())

# convert the object into a dict
styles_view_dict = styles_view_instance.to_dict()
# create an instance of StylesView from a dict
styles_view_from_dict = StylesView.from_dict(styles_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


