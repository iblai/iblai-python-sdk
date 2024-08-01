# TimeDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TimeDetailData]**](TimeDetailData.md) |  | [optional] 
**total** | **int** | Total time spent | [optional] 

## Example

```python
from iblai.models.time_detail import TimeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TimeDetail from a JSON string
time_detail_instance = TimeDetail.from_json(json)
# print the JSON string representation of the object
print(TimeDetail.to_json())

# convert the object into a dict
time_detail_dict = time_detail_instance.to_dict()
# create an instance of TimeDetail from a dict
time_detail_from_dict = TimeDetail.from_dict(time_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


