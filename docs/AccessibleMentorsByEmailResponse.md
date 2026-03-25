# AccessibleMentorsByEmailResponse

Response serializer for accessible mentors by email.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentors** | **List[str]** | List of mentor unique IDs | [readonly] 
**user_id** | **int** | The user ID that mentors belong to when all_mentors is False | [readonly] 

## Example

```python
from iblai.models.accessible_mentors_by_email_response import AccessibleMentorsByEmailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessibleMentorsByEmailResponse from a JSON string
accessible_mentors_by_email_response_instance = AccessibleMentorsByEmailResponse.from_json(json)
# print the JSON string representation of the object
print(AccessibleMentorsByEmailResponse.to_json())

# convert the object into a dict
accessible_mentors_by_email_response_dict = accessible_mentors_by_email_response_instance.to_dict()
# create an instance of AccessibleMentorsByEmailResponse from a dict
accessible_mentors_by_email_response_from_dict = AccessibleMentorsByEmailResponse.from_dict(accessible_mentors_by_email_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


