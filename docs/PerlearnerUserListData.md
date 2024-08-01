# PerlearnerUserListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | learner username | 
**full_name** | **str** | learner Name | 
**enrollments** | **int** | Total enrollments | 
**completions** | **int** | Total completions | 
**last_active** | **str** | Last active time | 
**time_spent** | **str** | Time spent formatted in seconds | 
**engagement_index** | **float** | Engagement index | 
**performance_index** | **float** | Performance index | 

## Example

```python
from iblai.models.perlearner_user_list_data import PerlearnerUserListData

# TODO update the JSON string below
json = "{}"
# create an instance of PerlearnerUserListData from a JSON string
perlearner_user_list_data_instance = PerlearnerUserListData.from_json(json)
# print the JSON string representation of the object
print(PerlearnerUserListData.to_json())

# convert the object into a dict
perlearner_user_list_data_dict = perlearner_user_list_data_instance.to_dict()
# create an instance of PerlearnerUserListData from a dict
perlearner_user_list_data_from_dict = PerlearnerUserListData.from_dict(perlearner_user_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


