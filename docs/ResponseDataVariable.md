# ResponseDataVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_name** | **str** | Variable Name | 
**predicted_data** | **object** | Predicted data | 
**narrative** | **str** | Explanation of prediction | 

## Example

```python
from iblai.models.response_data_variable import ResponseDataVariable

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDataVariable from a JSON string
response_data_variable_instance = ResponseDataVariable.from_json(json)
# print the JSON string representation of the object
print(ResponseDataVariable.to_json())

# convert the object into a dict
response_data_variable_dict = response_data_variable_instance.to_dict()
# create an instance of ResponseDataVariable from a dict
response_data_variable_from_dict = ResponseDataVariable.from_dict(response_data_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


