# PaginatedPeriodicAgentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PeriodicAgent]**](PeriodicAgent.md) |  | [optional] 

## Example

```python
from iblai.models.paginated_periodic_agent_list import PaginatedPeriodicAgentList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPeriodicAgentList from a JSON string
paginated_periodic_agent_list_instance = PaginatedPeriodicAgentList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPeriodicAgentList.to_json())

# convert the object into a dict
paginated_periodic_agent_list_dict = paginated_periodic_agent_list_instance.to_dict()
# create an instance of PaginatedPeriodicAgentList from a dict
paginated_periodic_agent_list_from_dict = PaginatedPeriodicAgentList.from_dict(paginated_periodic_agent_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


