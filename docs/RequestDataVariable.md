# RequestDataVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_name** | **str** | Variable Name | 
**data_set** | **object** | Data set to be used for prediction | 
**number_of_data_points** | **int** | Number of Data Points | 

## Example

```python
from iblai.models.request_data_variable import RequestDataVariable

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDataVariable from a JSON string
request_data_variable_instance = RequestDataVariable.from_json(json)
# print the JSON string representation of the object
print(RequestDataVariable.to_json())

# convert the object into a dict
request_data_variable_dict = request_data_variable_instance.to_dict()
# create an instance of RequestDataVariable from a dict
request_data_variable_from_dict = RequestDataVariable.from_dict(request_data_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


