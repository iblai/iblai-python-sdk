# Trace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**timestamp** | **datetime** |  | 
**name** | **str** |  | 
**user_id** | **str** |  | [optional] 
**metadata** | **object** |  | 
**release** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**tags** | **List[str]** |  | 
**input** | **str** |  | [optional] 
**output** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] 
**event_ts** | **datetime** |  | 
**is_deleted** | **int** |  | 

## Example

```python
from iblai.models.trace import Trace

# TODO update the JSON string below
json = "{}"
# create an instance of Trace from a JSON string
trace_instance = Trace.from_json(json)
# print the JSON string representation of the object
print(Trace.to_json())

# convert the object into a dict
trace_dict = trace_instance.to_dict()
# create an instance of Trace from a dict
trace_from_dict = Trace.from_dict(trace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


