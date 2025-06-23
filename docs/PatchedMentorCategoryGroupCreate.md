# PatchedMentorCategoryGroupCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**audience** | **int** | Deprecated: This is only left for backward compatibility. Please use the audiences field instead. | [optional] 
**audiences** | **List[int]** |  | [optional] 
**date_created** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_mentor_category_group_create import PatchedMentorCategoryGroupCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMentorCategoryGroupCreate from a JSON string
patched_mentor_category_group_create_instance = PatchedMentorCategoryGroupCreate.from_json(json)
# print the JSON string representation of the object
print(PatchedMentorCategoryGroupCreate.to_json())

# convert the object into a dict
patched_mentor_category_group_create_dict = patched_mentor_category_group_create_instance.to_dict()
# create an instance of PatchedMentorCategoryGroupCreate from a dict
patched_mentor_category_group_create_from_dict = PatchedMentorCategoryGroupCreate.from_dict(patched_mentor_category_group_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


