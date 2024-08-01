# EngagementPerCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EngagementPerCourseData]**](EngagementPerCourseData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from iblai.models.engagement_per_course import EngagementPerCourse

# TODO update the JSON string below
json = "{}"
# create an instance of EngagementPerCourse from a JSON string
engagement_per_course_instance = EngagementPerCourse.from_json(json)
# print the JSON string representation of the object
print(EngagementPerCourse.to_json())

# convert the object into a dict
engagement_per_course_dict = engagement_per_course_instance.to_dict()
# create an instance of EngagementPerCourse from a dict
engagement_per_course_from_dict = EngagementPerCourse.from_dict(engagement_per_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


