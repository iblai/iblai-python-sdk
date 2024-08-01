# TonesView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**description** | **str** |  | [optional] 

## Example

```python
from iblai.models.tones_view import TonesView

# TODO update the JSON string below
json = "{}"
# create an instance of TonesView from a JSON string
tones_view_instance = TonesView.from_json(json)
# print the JSON string representation of the object
print(TonesView.to_json())

# convert the object into a dict
tones_view_dict = tones_view_instance.to_dict()
# create an instance of TonesView from a dict
tones_view_from_dict = TonesView.from_dict(tones_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


