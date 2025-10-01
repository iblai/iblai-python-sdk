# PaginatedTraceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Trace]**](Trace.md) |  | 

## Example

```python
from iblai.models.paginated_trace_list import PaginatedTraceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTraceList from a JSON string
paginated_trace_list_instance = PaginatedTraceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTraceList.to_json())

# convert the object into a dict
paginated_trace_list_dict = paginated_trace_list_instance.to_dict()
# create an instance of PaginatedTraceList from a dict
paginated_trace_list_from_dict = PaginatedTraceList.from_dict(paginated_trace_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


