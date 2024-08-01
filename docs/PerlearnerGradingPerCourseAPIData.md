# PerlearnerGradingPerCourseAPIData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | Edx Course ID | 
**name** | **str** | Course Name | 
**graded_activities** | **str** | Total problems in course | 
**submissions** | **int** | Cumulative problem submissions | 
**problems_attempted** | **int** | Number of problems from total problems attempted | 
**assignments_correct** | **int** | Number of problems answered correctly | 
**class_average** | **float** | Average grade obtained by all learner in the course | 
**grade** | **float** | Learner course grade | 

## Example

```python
from iblai.models.perlearner_grading_per_course_api_data import PerlearnerGradingPerCourseAPIData

# TODO update the JSON string below
json = "{}"
# create an instance of PerlearnerGradingPerCourseAPIData from a JSON string
perlearner_grading_per_course_api_data_instance = PerlearnerGradingPerCourseAPIData.from_json(json)
# print the JSON string representation of the object
print(PerlearnerGradingPerCourseAPIData.to_json())

# convert the object into a dict
perlearner_grading_per_course_api_data_dict = perlearner_grading_per_course_api_data_instance.to_dict()
# create an instance of PerlearnerGradingPerCourseAPIData from a dict
perlearner_grading_per_course_api_data_from_dict = PerlearnerGradingPerCourseAPIData.from_dict(perlearner_grading_per_course_api_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


