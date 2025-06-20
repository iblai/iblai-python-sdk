# MentorCategoryCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**category_group** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**audience** | **int** | Deprecated: This is only left for backward compatibility. Please use the audiences field instead. | [optional] 
**audiences** | **List[int]** |  | [optional] 

## Example

```python
from iblai.models.mentor_category_create import MentorCategoryCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MentorCategoryCreate from a JSON string
mentor_category_create_instance = MentorCategoryCreate.from_json(json)
# print the JSON string representation of the object
print(MentorCategoryCreate.to_json())

# convert the object into a dict
mentor_category_create_dict = mentor_category_create_instance.to_dict()
# create an instance of MentorCategoryCreate from a dict
mentor_category_create_from_dict = MentorCategoryCreate.from_dict(mentor_category_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


