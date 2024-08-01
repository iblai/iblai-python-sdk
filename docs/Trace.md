# Trace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | [optional] 
**external_id** | **str** |  | 
**timestamp** | **datetime** |  | 
**name** | **str** |  | 
**totalprice** | **float** |  | 
**user_id** | **str** |  | 
**metadata** | **Dict[str, object]** |  | 
**release** | **str** |  | 
**version** | **str** |  | 
**project_id** | **str** |  | 
**public** | **bool** |  | 
**bookmarked** | **bool** |  | 
**tags** | **List[str]** |  | 
**input** | **object** |  | 
**output** | **object** |  | 
**session_id** | **str** |  | 
**scores** | **List[Dict[str, object]]** |  | 
**observations** | [**List[Observation]**](Observation.md) |  | 

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


