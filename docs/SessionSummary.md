# SessionSummary

Lightweight serializer for session list endpoints (pinned/recent messages).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 
**mentor_unique_id** | **str** |  | 
**mentor** | [**SessionSummaryMentor**](SessionSummaryMentor.md) |  | 
**title** | **str** |  | 
**messages** | [**List[ChatHistory]**](ChatHistory.md) |  | 

## Example

```python
from iblai.models.session_summary import SessionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SessionSummary from a JSON string
session_summary_instance = SessionSummary.from_json(json)
# print the JSON string representation of the object
print(SessionSummary.to_json())

# convert the object into a dict
session_summary_dict = session_summary_instance.to_dict()
# create an instance of SessionSummary from a dict
session_summary_from_dict = SessionSummary.from_dict(session_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


