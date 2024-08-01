# OvertimeWithChangeInfo

Returns     {         \"data\": {             \"2022-04-26\": 0,             \"2022-04-27\": 0,             ...             \"2023-01-01\": 0         },         \"total\": 0     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | Dates are keys and values are the value for the date in the key. e,g &#x60;{\&quot;2020-01-01\&quot;: 30. ...}&#x60; | [optional] 
**total** | **int** | Total | [optional] 
**meta** | [**OvertimeMeta**](OvertimeMeta.md) |  | 

## Example

```python
from iblai.models.overtime_with_change_info import OvertimeWithChangeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OvertimeWithChangeInfo from a JSON string
overtime_with_change_info_instance = OvertimeWithChangeInfo.from_json(json)
# print the JSON string representation of the object
print(OvertimeWithChangeInfo.to_json())

# convert the object into a dict
overtime_with_change_info_dict = overtime_with_change_info_instance.to_dict()
# create an instance of OvertimeWithChangeInfo from a dict
overtime_with_change_info_from_dict = OvertimeWithChangeInfo.from_dict(overtime_with_change_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


