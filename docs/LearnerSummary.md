# LearnerSummary

Serializer for learner summary data across all platforms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_time_spent_seconds** | **int** | Total time spent across all platforms | 

## Example

```python
from iblai.models.learner_summary import LearnerSummary

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerSummary from a JSON string
learner_summary_instance = LearnerSummary.from_json(json)
# print the JSON string representation of the object
print(LearnerSummary.to_json())

# convert the object into a dict
learner_summary_dict = learner_summary_instance.to_dict()
# create an instance of LearnerSummary from a dict
learner_summary_from_dict = LearnerSummary.from_dict(learner_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


