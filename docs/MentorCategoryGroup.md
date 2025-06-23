# MentorCategoryGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | 
**audience** | [**MentorAudience**](MentorAudience.md) |  | 
**date_created** | **datetime** |  | [readonly] 
**categories** | [**List[MentorCategory]**](MentorCategory.md) |  | 
**audiences** | [**List[MentorAudience]**](MentorAudience.md) |  | 

## Example

```python
from iblai.models.mentor_category_group import MentorCategoryGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MentorCategoryGroup from a JSON string
mentor_category_group_instance = MentorCategoryGroup.from_json(json)
# print the JSON string representation of the object
print(MentorCategoryGroup.to_json())

# convert the object into a dict
mentor_category_group_dict = mentor_category_group_instance.to_dict()
# create an instance of MentorCategoryGroup from a dict
mentor_category_group_from_dict = MentorCategoryGroup.from_dict(mentor_category_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


