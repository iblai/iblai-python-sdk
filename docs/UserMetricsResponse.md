# UserMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registered_users** | [**UserMetric**](UserMetric.md) |  | 
**new_users** | [**UserMetric**](UserMetric.md) |  | 
**unique_users** | [**UserMetric**](UserMetric.md) |  | 
**veteran_users** | [**UserMetric**](UserMetric.md) |  | 

## Example

```python
from iblai.models.user_metrics_response import UserMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserMetricsResponse from a JSON string
user_metrics_response_instance = UserMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(UserMetricsResponse.to_json())

# convert the object into a dict
user_metrics_response_dict = user_metrics_response_instance.to_dict()
# create an instance of UserMetricsResponse from a dict
user_metrics_response_from_dict = UserMetricsResponse.from_dict(user_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


