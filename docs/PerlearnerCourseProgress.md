# PerlearnerCourseProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PerlearnerCourseProgressData**](PerlearnerCourseProgressData.md) |  | 

## Example

```python
from iblai.models.perlearner_course_progress import PerlearnerCourseProgress

# TODO update the JSON string below
json = "{}"
# create an instance of PerlearnerCourseProgress from a JSON string
perlearner_course_progress_instance = PerlearnerCourseProgress.from_json(json)
# print the JSON string representation of the object
print(PerlearnerCourseProgress.to_json())

# convert the object into a dict
perlearner_course_progress_dict = perlearner_course_progress_instance.to_dict()
# create an instance of PerlearnerCourseProgress from a dict
perlearner_course_progress_from_dict = PerlearnerCourseProgress.from_dict(perlearner_course_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


