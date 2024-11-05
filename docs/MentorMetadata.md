# MentorMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | 
**mentor** | **str** |  | [optional] 
**mentor_id** | **int** |  | [optional] 

## Example

```python
from iblai.models.mentor_metadata import MentorMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MentorMetadata from a JSON string
mentor_metadata_instance = MentorMetadata.from_json(json)
# print the JSON string representation of the object
print(MentorMetadata.to_json())

# convert the object into a dict
mentor_metadata_dict = mentor_metadata_instance.to_dict()
# create an instance of MentorMetadata from a dict
mentor_metadata_from_dict = MentorMetadata.from_dict(mentor_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


