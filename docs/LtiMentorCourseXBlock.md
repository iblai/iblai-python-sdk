# LtiMentorCourseXBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentor** | **str** | The unique_id of the mentor | 
**location** | **str** | The xblock location of the mentor | [readonly] 

## Example

```python
from iblai.models.lti_mentor_course_x_block import LtiMentorCourseXBlock

# TODO update the JSON string below
json = "{}"
# create an instance of LtiMentorCourseXBlock from a JSON string
lti_mentor_course_x_block_instance = LtiMentorCourseXBlock.from_json(json)
# print the JSON string representation of the object
print(LtiMentorCourseXBlock.to_json())

# convert the object into a dict
lti_mentor_course_x_block_dict = lti_mentor_course_x_block_instance.to_dict()
# create an instance of LtiMentorCourseXBlock from a dict
lti_mentor_course_x_block_from_dict = LtiMentorCourseXBlock.from_dict(lti_mentor_course_x_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


