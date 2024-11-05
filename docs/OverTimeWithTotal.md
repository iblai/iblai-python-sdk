# OverTimeWithTotal

Returns     {         \"data\": {             \"2022-04-26\": 0,             \"2022-04-27\": 0,             ...             \"2023-01-01\": 0         },         \"total\": 0     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | Dates are keys and values are the value for the date in the key. e,g &#x60;{\&quot;2020-01-01\&quot;: 30. ...}&#x60; | [optional] 
**total** | **int** | Total | [optional] 

## Example

```python
from iblai.models.over_time_with_total import OverTimeWithTotal

# TODO update the JSON string below
json = "{}"
# create an instance of OverTimeWithTotal from a JSON string
over_time_with_total_instance = OverTimeWithTotal.from_json(json)
# print the JSON string representation of the object
print(OverTimeWithTotal.to_json())

# convert the object into a dict
over_time_with_total_dict = over_time_with_total_instance.to_dict()
# create an instance of OverTimeWithTotal from a dict
over_time_with_total_from_dict = OverTimeWithTotal.from_dict(over_time_with_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


