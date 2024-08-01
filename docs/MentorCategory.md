# MentorCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from iblai.models.mentor_category import MentorCategory

# TODO update the JSON string below
json = "{}"
# create an instance of MentorCategory from a JSON string
mentor_category_instance = MentorCategory.from_json(json)
# print the JSON string representation of the object
print(MentorCategory.to_json())

# convert the object into a dict
mentor_category_dict = mentor_category_instance.to_dict()
# create an instance of MentorCategory from a dict
mentor_category_from_dict = MentorCategory.from_dict(mentor_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


