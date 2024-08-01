# ValueData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | value | 

## Example

```python
from iblai.models.value_data import ValueData

# TODO update the JSON string below
json = "{}"
# create an instance of ValueData from a JSON string
value_data_instance = ValueData.from_json(json)
# print the JSON string representation of the object
print(ValueData.to_json())

# convert the object into a dict
value_data_dict = value_data_instance.to_dict()
# create an instance of ValueData from a dict
value_data_from_dict = ValueData.from_dict(value_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


