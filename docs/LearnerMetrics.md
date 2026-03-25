# LearnerMetrics

Serializer for learner metrics from UserPlatformSummary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollments** | **int** | Total enrollments | 
**programs** | **int** | Total programs | 
**pathways** | **int** | Total pathways | 
**resources** | **int** | Total resources | 
**reported_skills** | **int** | Reported skills count | 
**desired_skills** | **int** | Desired skills count | 
**assigned_skills** | **int** | Assigned skills count | 
**total_skills** | **int** | Total skills count | 
**credentials** | **int** | Credentials earned | 
**points** | **float** | Total points | 
**total_time_spent_seconds** | **int** | Total time spent in seconds | 
**top_content** | [**TopContent**](TopContent.md) | Course with most time spent | 

## Example

```python
from iblai.models.learner_metrics import LearnerMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerMetrics from a JSON string
learner_metrics_instance = LearnerMetrics.from_json(json)
# print the JSON string representation of the object
print(LearnerMetrics.to_json())

# convert the object into a dict
learner_metrics_dict = learner_metrics_instance.to_dict()
# create an instance of LearnerMetrics from a dict
learner_metrics_from_dict = LearnerMetrics.from_dict(learner_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


