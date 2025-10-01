# UserDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**full_name** | **str** |  | 
**messages** | **int** |  | 
**conversations** | **int** |  | 
**last_activity** | **datetime** |  | 

## Example

```python
from iblai.models.user_detail import UserDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetail from a JSON string
user_detail_instance = UserDetail.from_json(json)
# print the JSON string representation of the object
print(UserDetail.to_json())

# convert the object into a dict
user_detail_dict = user_detail_instance.to_dict()
# create an instance of UserDetail from a dict
user_detail_from_dict = UserDetail.from_dict(user_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


