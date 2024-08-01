# FloatOverTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of event | 
**total** | **float** | Total quantity for date | 

## Example

```python
from iblai.models.float_over_time import FloatOverTime

# TODO update the JSON string below
json = "{}"
# create an instance of FloatOverTime from a JSON string
float_over_time_instance = FloatOverTime.from_json(json)
# print the JSON string representation of the object
print(FloatOverTime.to_json())

# convert the object into a dict
float_over_time_dict = float_over_time_instance.to_dict()
# create an instance of FloatOverTime from a dict
float_over_time_from_dict = FloatOverTime.from_dict(float_over_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


