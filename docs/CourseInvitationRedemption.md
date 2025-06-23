# CourseInvitationRedemption

Request serializer for CourseInvitationRedemptionView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | The course ID for the invitation | 
**source** | **str** | The source identifier for the invitation | 
**email** | **str** | The email to associate with the invitation | [optional] 
**username** | **str** | The username to associate with the invitation | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the invitation | [optional] 

## Example

```python
from iblai.models.course_invitation_redemption import CourseInvitationRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of CourseInvitationRedemption from a JSON string
course_invitation_redemption_instance = CourseInvitationRedemption.from_json(json)
# print the JSON string representation of the object
print(CourseInvitationRedemption.to_json())

# convert the object into a dict
course_invitation_redemption_dict = course_invitation_redemption_instance.to_dict()
# create an instance of CourseInvitationRedemption from a dict
course_invitation_redemption_from_dict = CourseInvitationRedemption.from_dict(course_invitation_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


