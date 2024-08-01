# GradingPerUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GradingPerUserData]**](GradingPerUserData.md) |  | [optional] 
**total** | **int** | Total rows | [optional] 

## Example

```python
from iblai.models.grading_per_user import GradingPerUser

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPerUser from a JSON string
grading_per_user_instance = GradingPerUser.from_json(json)
# print the JSON string representation of the object
print(GradingPerUser.to_json())

# convert the object into a dict
grading_per_user_dict = grading_per_user_instance.to_dict()
# create an instance of GradingPerUser from a dict
grading_per_user_from_dict = GradingPerUser.from_dict(grading_per_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


