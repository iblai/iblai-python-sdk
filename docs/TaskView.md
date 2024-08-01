# TaskView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 

## Example

```python
from iblai.models.task_view import TaskView

# TODO update the JSON string below
json = "{}"
# create an instance of TaskView from a JSON string
task_view_instance = TaskView.from_json(json)
# print the JSON string representation of the object
print(TaskView.to_json())

# convert the object into a dict
task_view_dict = task_view_instance.to_dict()
# create an instance of TaskView from a dict
task_view_from_dict = TaskView.from_dict(task_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


