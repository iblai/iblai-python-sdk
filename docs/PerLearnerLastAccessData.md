# PerLearnerLastAccessData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_last_accessed** | [**PerLearnerCourseLastAccessData**](PerLearnerCourseLastAccessData.md) | Course last accessed metadata | [optional] 
**last_accessed** | **str** | Last accessed time | [optional] 

## Example

```python
from iblai.models.per_learner_last_access_data import PerLearnerLastAccessData

# TODO update the JSON string below
json = "{}"
# create an instance of PerLearnerLastAccessData from a JSON string
per_learner_last_access_data_instance = PerLearnerLastAccessData.from_json(json)
# print the JSON string representation of the object
print(PerLearnerLastAccessData.to_json())

# convert the object into a dict
per_learner_last_access_data_dict = per_learner_last_access_data_instance.to_dict()
# create an instance of PerLearnerLastAccessData from a dict
per_learner_last_access_data_from_dict = PerLearnerLastAccessData.from_dict(per_learner_last_access_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


