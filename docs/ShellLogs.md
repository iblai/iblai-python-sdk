# ShellLogs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | **str** |  | 

## Example

```python
from iblai.models.shell_logs import ShellLogs

# TODO update the JSON string below
json = "{}"
# create an instance of ShellLogs from a JSON string
shell_logs_instance = ShellLogs.from_json(json)
# print the JSON string representation of the object
print(ShellLogs.to_json())

# convert the object into a dict
shell_logs_dict = shell_logs_instance.to_dict()
# create an instance of ShellLogs from a dict
shell_logs_from_dict = ShellLogs.from_dict(shell_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


