# ActiveUsersData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | learner username | 
**name** | **str** | learner name | 
**engagement_index** | **float** | Engagement index | 
**performance_index** | **float** | Performance index | 

## Example

```python
from iblai.models.active_users_data import ActiveUsersData

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveUsersData from a JSON string
active_users_data_instance = ActiveUsersData.from_json(json)
# print the JSON string representation of the object
print(ActiveUsersData.to_json())

# convert the object into a dict
active_users_data_dict = active_users_data_instance.to_dict()
# create an instance of ActiveUsersData from a dict
active_users_data_from_dict = ActiveUsersData.from_dict(active_users_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


