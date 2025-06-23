# TrendEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **datetime** |  | 
**count** | **int** |  | 

## Example

```python
from iblai.models.trend_entry import TrendEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TrendEntry from a JSON string
trend_entry_instance = TrendEntry.from_json(json)
# print the JSON string representation of the object
print(TrendEntry.to_json())

# convert the object into a dict
trend_entry_dict = trend_entry_instance.to_dict()
# create an instance of TrendEntry from a dict
trend_entry_from_dict = TrendEntry.from_dict(trend_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


