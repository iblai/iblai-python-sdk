# UserTrendByPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periods** | **List[datetime]** |  | 
**new_users** | **List[int]** |  | 
**veteran_users** | **List[int]** |  | 

## Example

```python
from iblai.models.user_trend_by_period import UserTrendByPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of UserTrendByPeriod from a JSON string
user_trend_by_period_instance = UserTrendByPeriod.from_json(json)
# print the JSON string representation of the object
print(UserTrendByPeriod.to_json())

# convert the object into a dict
user_trend_by_period_dict = user_trend_by_period_instance.to_dict()
# create an instance of UserTrendByPeriod from a dict
user_trend_by_period_from_dict = UserTrendByPeriod.from_dict(user_trend_by_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


