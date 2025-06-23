# UserMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**change_percentage** | **float** |  | 

## Example

```python
from iblai.models.user_metric import UserMetric

# TODO update the JSON string below
json = "{}"
# create an instance of UserMetric from a JSON string
user_metric_instance = UserMetric.from_json(json)
# print the JSON string representation of the object
print(UserMetric.to_json())

# convert the object into a dict
user_metric_dict = user_metric_instance.to_dict()
# create an instance of UserMetric from a dict
user_metric_from_dict = UserMetric.from_dict(user_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


