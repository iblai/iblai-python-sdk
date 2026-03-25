# LearnerAnalyticsResult

Unified serializer for learner analytics results - handles both cross-platform and platform-specific data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_id** | **int** |  | 
**platform_name** | **str** |  | 
**platform_key** | **str** |  | 
**summary** | [**PlatformSummary**](PlatformSummary.md) |  | [optional] 
**metrics** | [**PlatformMetrics**](PlatformMetrics.md) |  | [optional] 
**activity** | [**ActivityInfo**](ActivityInfo.md) |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from iblai.models.learner_analytics_result import LearnerAnalyticsResult

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerAnalyticsResult from a JSON string
learner_analytics_result_instance = LearnerAnalyticsResult.from_json(json)
# print the JSON string representation of the object
print(LearnerAnalyticsResult.to_json())

# convert the object into a dict
learner_analytics_result_dict = learner_analytics_result_instance.to_dict()
# create an instance of LearnerAnalyticsResult from a dict
learner_analytics_result_from_dict = LearnerAnalyticsResult.from_dict(learner_analytics_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


