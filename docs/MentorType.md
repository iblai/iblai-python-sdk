# MentorType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from iblai.models.mentor_type import MentorType

# TODO update the JSON string below
json = "{}"
# create an instance of MentorType from a JSON string
mentor_type_instance = MentorType.from_json(json)
# print the JSON string representation of the object
print(MentorType.to_json())

# convert the object into a dict
mentor_type_dict = mentor_type_instance.to_dict()
# create an instance of MentorType from a dict
mentor_type_from_dict = MentorType.from_dict(mentor_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


