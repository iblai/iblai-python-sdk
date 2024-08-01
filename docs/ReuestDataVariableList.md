# ReuestDataVariableList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_variables** | [**List[RequestDataVariable]**](RequestDataVariable.md) |  | 

## Example

```python
from iblai.models.reuest_data_variable_list import ReuestDataVariableList

# TODO update the JSON string below
json = "{}"
# create an instance of ReuestDataVariableList from a JSON string
reuest_data_variable_list_instance = ReuestDataVariableList.from_json(json)
# print the JSON string representation of the object
print(ReuestDataVariableList.to_json())

# convert the object into a dict
reuest_data_variable_list_dict = reuest_data_variable_list_instance.to_dict()
# create an instance of ReuestDataVariableList from a dict
reuest_data_variable_list_from_dict = ReuestDataVariableList.from_dict(reuest_data_variable_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


