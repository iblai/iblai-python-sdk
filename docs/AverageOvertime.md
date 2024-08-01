# AverageOvertime

Returns     {         \"data\": {             \"2022-04-26\": 0,             \"2022-04-27\": 0,             ...             \"2023-01-01\": 0         },         \"average\": 0     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | Dates are keys and values are the value for the date in the key. e,g &#x60;{\&quot;2020-01-01\&quot;: 30. ...}&#x60; | [optional] 
**average** | **float** | average | [optional] 

## Example

```python
from iblai.models.average_overtime import AverageOvertime

# TODO update the JSON string below
json = "{}"
# create an instance of AverageOvertime from a JSON string
average_overtime_instance = AverageOvertime.from_json(json)
# print the JSON string representation of the object
print(AverageOvertime.to_json())

# convert the object into a dict
average_overtime_dict = average_overtime_instance.to_dict()
# create an instance of AverageOvertime from a dict
average_overtime_from_dict = AverageOvertime.from_dict(average_overtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


