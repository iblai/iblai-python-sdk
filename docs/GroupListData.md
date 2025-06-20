# GroupListData

Serializer for department list endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**platform** | **str** |  | 
**courses_enrolled** | **int** |  | 
**courses_completed** | **int** |  | 
**completion_rate** | **float** |  | 
**pathways_completed** | **int** |  | 
**certificates_earned** | **int** |  | 
**skills_points** | **int** |  | 
**skills_earned** | **int** |  | 
**time_spent** | **str** |  | 

## Example

```python
from iblai.models.group_list_data import GroupListData

# TODO update the JSON string below
json = "{}"
# create an instance of GroupListData from a JSON string
group_list_data_instance = GroupListData.from_json(json)
# print the JSON string representation of the object
print(GroupListData.to_json())

# convert the object into a dict
group_list_data_dict = group_list_data_instance.to_dict()
# create an instance of GroupListData from a dict
group_list_data_from_dict = GroupListData.from_dict(group_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


