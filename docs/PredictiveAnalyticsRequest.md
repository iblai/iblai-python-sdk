# PredictiveAnalyticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | [**ReuestDataVariableList**](ReuestDataVariableList.md) |  | 

## Example

```python
from iblai.models.predictive_analytics_request import PredictiveAnalyticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PredictiveAnalyticsRequest from a JSON string
predictive_analytics_request_instance = PredictiveAnalyticsRequest.from_json(json)
# print the JSON string representation of the object
print(PredictiveAnalyticsRequest.to_json())

# convert the object into a dict
predictive_analytics_request_dict = predictive_analytics_request_instance.to_dict()
# create an instance of PredictiveAnalyticsRequest from a dict
predictive_analytics_request_from_dict = PredictiveAnalyticsRequest.from_dict(predictive_analytics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


