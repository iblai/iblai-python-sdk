# RetrieveTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | **str** |  | 

## Example

```python
from iblai.models.retrieve_task import RetrieveTask

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveTask from a JSON string
retrieve_task_instance = RetrieveTask.from_json(json)
# print the JSON string representation of the object
print(RetrieveTask.to_json())

# convert the object into a dict
retrieve_task_dict = retrieve_task_instance.to_dict()
# create an instance of RetrieveTask from a dict
retrieve_task_from_dict = RetrieveTask.from_dict(retrieve_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


