# PerLearnerCourseLastAccessData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | Edx Course ID | [optional] 
**course_name** | **str** | Course Name | [optional] 
**block_id** | **str** | Last Block Accessed | [optional] 
**block_display_name** | **str** | Last Block Display Name | [optional] 
**course_grade** | **float** | Course grade | [optional] 
**course_progress** | **float** | Course progress | [optional] 
**last_accessed** | **str** | Last accessed time | [optional] 

## Example

```python
from iblai.models.per_learner_course_last_access_data import PerLearnerCourseLastAccessData

# TODO update the JSON string below
json = "{}"
# create an instance of PerLearnerCourseLastAccessData from a JSON string
per_learner_course_last_access_data_instance = PerLearnerCourseLastAccessData.from_json(json)
# print the JSON string representation of the object
print(PerLearnerCourseLastAccessData.to_json())

# convert the object into a dict
per_learner_course_last_access_data_dict = per_learner_course_last_access_data_instance.to_dict()
# create an instance of PerLearnerCourseLastAccessData from a dict
per_learner_course_last_access_data_from_dict = PerLearnerCourseLastAccessData.from_dict(per_learner_course_last_access_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


