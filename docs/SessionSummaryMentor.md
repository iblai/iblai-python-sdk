# SessionSummaryMentor

Lightweight mentor serializer for backward compatibility.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** |  | 

## Example

```python
from iblai.models.session_summary_mentor import SessionSummaryMentor

# TODO update the JSON string below
json = "{}"
# create an instance of SessionSummaryMentor from a JSON string
session_summary_mentor_instance = SessionSummaryMentor.from_json(json)
# print the JSON string representation of the object
print(SessionSummaryMentor.to_json())

# convert the object into a dict
session_summary_mentor_dict = session_summary_mentor_instance.to_dict()
# create an instance of SessionSummaryMentor from a dict
session_summary_mentor_from_dict = SessionSummaryMentor.from_dict(session_summary_mentor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


