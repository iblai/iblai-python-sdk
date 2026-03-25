# LearnerAnalyticsResponse

Unified response serializer for learner analytics endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserInfo**](UserInfo.md) |  | 
**summary** | [**LearnerSummary**](LearnerSummary.md) |  | 
**results** | [**List[LearnerAnalyticsResult]**](LearnerAnalyticsResult.md) |  | 
**pagination** | [**Pagination**](Pagination.md) |  | 
**overtime** | [**List[OvertimeDataPoint]**](OvertimeDataPoint.md) | Time spent over time data (when overtime&#x3D;true) | [optional] 
**generated_at** | **datetime** |  | 

## Example

```python
from iblai.models.learner_analytics_response import LearnerAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerAnalyticsResponse from a JSON string
learner_analytics_response_instance = LearnerAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerAnalyticsResponse.to_json())

# convert the object into a dict
learner_analytics_response_dict = learner_analytics_response_instance.to_dict()
# create an instance of LearnerAnalyticsResponse from a dict
learner_analytics_response_from_dict = LearnerAnalyticsResponse.from_dict(learner_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


