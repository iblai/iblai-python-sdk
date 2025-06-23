# CourseSkillPointInfoRequest

Request serializer for CourseSkillPointInfoView POST endpoint. Validates request body for updating course skill point information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | ID of the course to update skill point information for | 
**point_data** | **Dict[str, int]** | Dictionary mapping skill names to point values. Example: {&#39;skill_name&#39;: 5} | 
**overwrite** | **bool** | If True, removes all skills not in point_data. If False, only updates specified skills. | [optional] [default to True]

## Example

```python
from iblai.models.course_skill_point_info_request import CourseSkillPointInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CourseSkillPointInfoRequest from a JSON string
course_skill_point_info_request_instance = CourseSkillPointInfoRequest.from_json(json)
# print the JSON string representation of the object
print(CourseSkillPointInfoRequest.to_json())

# convert the object into a dict
course_skill_point_info_request_dict = course_skill_point_info_request_instance.to_dict()
# create an instance of CourseSkillPointInfoRequest from a dict
course_skill_point_info_request_from_dict = CourseSkillPointInfoRequest.from_dict(course_skill_point_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


