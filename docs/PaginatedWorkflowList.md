# PaginatedWorkflowList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Workflow]**](Workflow.md) |  | 

## Example

```python
from iblai.models.paginated_workflow_list import PaginatedWorkflowList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWorkflowList from a JSON string
paginated_workflow_list_instance = PaginatedWorkflowList.from_json(json)
# print the JSON string representation of the object
print(PaginatedWorkflowList.to_json())

# convert the object into a dict
paginated_workflow_list_dict = paginated_workflow_list_instance.to_dict()
# create an instance of PaginatedWorkflowList from a dict
paginated_workflow_list_from_dict = PaginatedWorkflowList.from_dict(paginated_workflow_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


