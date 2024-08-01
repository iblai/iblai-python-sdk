# LanguagesView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**code** | **str** |  | [optional] 

## Example

```python
from iblai.models.languages_view import LanguagesView

# TODO update the JSON string below
json = "{}"
# create an instance of LanguagesView from a JSON string
languages_view_instance = LanguagesView.from_json(json)
# print the JSON string representation of the object
print(LanguagesView.to_json())

# convert the object into a dict
languages_view_dict = languages_view_instance.to_dict()
# create an instance of LanguagesView from a dict
languages_view_from_dict = LanguagesView.from_dict(languages_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


