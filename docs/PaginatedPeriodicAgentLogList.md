# PaginatedPeriodicAgentLogList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PeriodicAgentLog]**](PeriodicAgentLog.md) |  | [optional] 

## Example

```python
from iblai.models.paginated_periodic_agent_log_list import PaginatedPeriodicAgentLogList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPeriodicAgentLogList from a JSON string
paginated_periodic_agent_log_list_instance = PaginatedPeriodicAgentLogList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPeriodicAgentLogList.to_json())

# convert the object into a dict
paginated_periodic_agent_log_list_dict = paginated_periodic_agent_log_list_instance.to_dict()
# create an instance of PaginatedPeriodicAgentLogList from a dict
paginated_periodic_agent_log_list_from_dict = PaginatedPeriodicAgentLogList.from_dict(paginated_periodic_agent_log_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


