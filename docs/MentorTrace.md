# MentorTrace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 
**cost** | **float** |  | 
**latency** | **float** |  | 
**username** | **str** |  | 

## Example

```python
from iblai.models.mentor_trace import MentorTrace

# TODO update the JSON string below
json = "{}"
# create an instance of MentorTrace from a JSON string
mentor_trace_instance = MentorTrace.from_json(json)
# print the JSON string representation of the object
print(MentorTrace.to_json())

# convert the object into a dict
mentor_trace_dict = mentor_trace_instance.to_dict()
# create an instance of MentorTrace from a dict
mentor_trace_from_dict = MentorTrace.from_dict(mentor_trace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


