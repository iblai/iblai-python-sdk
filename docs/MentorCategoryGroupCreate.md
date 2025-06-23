# MentorCategoryGroupCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | 
**audience** | **int** | Deprecated: This is only left for backward compatibility. Please use the audiences field instead. | [optional] 
**audiences** | **List[int]** |  | [optional] 
**date_created** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.mentor_category_group_create import MentorCategoryGroupCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MentorCategoryGroupCreate from a JSON string
mentor_category_group_create_instance = MentorCategoryGroupCreate.from_json(json)
# print the JSON string representation of the object
print(MentorCategoryGroupCreate.to_json())

# convert the object into a dict
mentor_category_group_create_dict = mentor_category_group_create_instance.to_dict()
# create an instance of MentorCategoryGroupCreate from a dict
mentor_category_group_create_from_dict = MentorCategoryGroupCreate.from_dict(mentor_category_group_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


