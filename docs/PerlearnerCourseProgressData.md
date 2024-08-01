# PerlearnerCourseProgressData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress** | **float** | Perlearner Course progress | 

## Example

```python
from iblai.models.perlearner_course_progress_data import PerlearnerCourseProgressData

# TODO update the JSON string below
json = "{}"
# create an instance of PerlearnerCourseProgressData from a JSON string
perlearner_course_progress_data_instance = PerlearnerCourseProgressData.from_json(json)
# print the JSON string representation of the object
print(PerlearnerCourseProgressData.to_json())

# convert the object into a dict
perlearner_course_progress_data_dict = perlearner_course_progress_data_instance.to_dict()
# create an instance of PerlearnerCourseProgressData from a dict
perlearner_course_progress_data_from_dict = PerlearnerCourseProgressData.from_dict(perlearner_course_progress_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


