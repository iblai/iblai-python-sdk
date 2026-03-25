# GrantMentorAccessRequest

Request serializer for granting LTI mentor access

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID to grant access to | 

## Example

```python
from iblai.models.grant_mentor_access_request import GrantMentorAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GrantMentorAccessRequest from a JSON string
grant_mentor_access_request_instance = GrantMentorAccessRequest.from_json(json)
# print the JSON string representation of the object
print(GrantMentorAccessRequest.to_json())

# convert the object into a dict
grant_mentor_access_request_dict = grant_mentor_access_request_instance.to_dict()
# create an instance of GrantMentorAccessRequest from a dict
grant_mentor_access_request_from_dict = GrantMentorAccessRequest.from_dict(grant_mentor_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


