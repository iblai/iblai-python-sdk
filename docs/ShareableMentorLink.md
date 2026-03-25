# ShareableMentorLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**mentor** | **int** |  | [readonly] 
**token** | **str** |  | [readonly] 
**enabled** | **bool** |  | [optional] 
**inserted_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.shareable_mentor_link import ShareableMentorLink

# TODO update the JSON string below
json = "{}"
# create an instance of ShareableMentorLink from a JSON string
shareable_mentor_link_instance = ShareableMentorLink.from_json(json)
# print the JSON string representation of the object
print(ShareableMentorLink.to_json())

# convert the object into a dict
shareable_mentor_link_dict = shareable_mentor_link_instance.to_dict()
# create an instance of ShareableMentorLink from a dict
shareable_mentor_link_from_dict = ShareableMentorLink.from_dict(shareable_mentor_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


