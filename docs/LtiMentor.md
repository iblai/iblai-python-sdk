# LtiMentor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | The name of the mentor | 
**org** | **str** | The org of the mentor | [readonly] 
**course_key** | **str** | The course key | [readonly] 
**mentor_config** | [**LtiMentorCourseXBlock**](LtiMentorCourseXBlock.md) |  | 
**platform_key** | **str** | Platform key the requesting user belongs to | 

## Example

```python
from iblai.models.lti_mentor import LtiMentor

# TODO update the JSON string below
json = "{}"
# create an instance of LtiMentor from a JSON string
lti_mentor_instance = LtiMentor.from_json(json)
# print the JSON string representation of the object
print(LtiMentor.to_json())

# convert the object into a dict
lti_mentor_dict = lti_mentor_instance.to_dict()
# create an instance of LtiMentor from a dict
lti_mentor_from_dict = LtiMentor.from_dict(lti_mentor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


