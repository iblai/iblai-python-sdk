# PaginatedAgentConfigList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AgentConfig]**](AgentConfig.md) |  | 

## Example

```python
from iblai.models.paginated_agent_config_list import PaginatedAgentConfigList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAgentConfigList from a JSON string
paginated_agent_config_list_instance = PaginatedAgentConfigList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAgentConfigList.to_json())

# convert the object into a dict
paginated_agent_config_list_dict = paginated_agent_config_list_instance.to_dict()
# create an instance of PaginatedAgentConfigList from a dict
paginated_agent_config_list_from_dict = PaginatedAgentConfigList.from_dict(paginated_agent_config_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


