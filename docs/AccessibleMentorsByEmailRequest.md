# AccessibleMentorsByEmailRequest

Request serializer for accessible mentors by email endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user email to check mentor access for | 
**all_mentors** | **bool** | If true, return all mentors in the platform. If false (default), return only mentors owned by the user&#39;s email. | [optional] [default to False]

## Example

```python
from iblai.models.accessible_mentors_by_email_request import AccessibleMentorsByEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessibleMentorsByEmailRequest from a JSON string
accessible_mentors_by_email_request_instance = AccessibleMentorsByEmailRequest.from_json(json)
# print the JSON string representation of the object
print(AccessibleMentorsByEmailRequest.to_json())

# convert the object into a dict
accessible_mentors_by_email_request_dict = accessible_mentors_by_email_request_instance.to_dict()
# create an instance of AccessibleMentorsByEmailRequest from a dict
accessible_mentors_by_email_request_from_dict = AccessibleMentorsByEmailRequest.from_dict(accessible_mentors_by_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


