# PaginatedMentorAuditLogEntryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MentorAuditLogEntry]**](MentorAuditLogEntry.md) |  | 

## Example

```python
from iblai.models.paginated_mentor_audit_log_entry_list import PaginatedMentorAuditLogEntryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMentorAuditLogEntryList from a JSON string
paginated_mentor_audit_log_entry_list_instance = PaginatedMentorAuditLogEntryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMentorAuditLogEntryList.to_json())

# convert the object into a dict
paginated_mentor_audit_log_entry_list_dict = paginated_mentor_audit_log_entry_list_instance.to_dict()
# create an instance of PaginatedMentorAuditLogEntryList from a dict
paginated_mentor_audit_log_entry_list_from_dict = PaginatedMentorAuditLogEntryList.from_dict(paginated_mentor_audit_log_entry_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


