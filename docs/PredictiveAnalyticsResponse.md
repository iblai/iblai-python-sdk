# PredictiveAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predictions** | [**List[ResponseDataVariable]**](ResponseDataVariable.md) |  | 

## Example

```python
from iblai.models.predictive_analytics_response import PredictiveAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PredictiveAnalyticsResponse from a JSON string
predictive_analytics_response_instance = PredictiveAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(PredictiveAnalyticsResponse.to_json())

# convert the object into a dict
predictive_analytics_response_dict = predictive_analytics_response_instance.to_dict()
# create an instance of PredictiveAnalyticsResponse from a dict
predictive_analytics_response_from_dict = PredictiveAnalyticsResponse.from_dict(predictive_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


