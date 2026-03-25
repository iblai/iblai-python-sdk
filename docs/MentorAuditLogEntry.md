# MentorAuditLogEntry

Serializer for a single audit log entry.  Transforms DMAuditLogEntry model instances into API response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Audit log entry ID | 
**timestamp** | **datetime** | When the action occurred | 
**actor_username** | **str** | Username of the user who performed the action | 
**action** | **str** | Action type: create, update, or delete | 
**resource_type** | **str** | Type of resource modified (e.g., mentor, mentorsettings) | 
**resource_id** | **str** | ID of the modified resource | 
**resource_repr** | **str** | Human-readable representation of the resource | 
**changes** | **Dict[str, object]** | Dictionary of field changes with old and new values | 

## Example

```python
from iblai.models.mentor_audit_log_entry import MentorAuditLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of MentorAuditLogEntry from a JSON string
mentor_audit_log_entry_instance = MentorAuditLogEntry.from_json(json)
# print the JSON string representation of the object
print(MentorAuditLogEntry.to_json())

# convert the object into a dict
mentor_audit_log_entry_dict = mentor_audit_log_entry_instance.to_dict()
# create an instance of MentorAuditLogEntry from a dict
mentor_audit_log_entry_from_dict = MentorAuditLogEntry.from_dict(mentor_audit_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


