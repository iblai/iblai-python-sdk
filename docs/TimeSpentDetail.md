# TimeSpentDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courses** | [**List[TimeSpentCourse]**](TimeSpentCourse.md) |  | 
**total_time_spent** | **str** |  | 
**total_time_spent_secs** | **int** |  | 
**overtime** | [**List[OvertimeDataPoint]**](OvertimeDataPoint.md) | Time spent over time data (when overtime&#x3D;true) | [optional] 

## Example

```python
from iblai.models.time_spent_detail import TimeSpentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpentDetail from a JSON string
time_spent_detail_instance = TimeSpentDetail.from_json(json)
# print the JSON string representation of the object
print(TimeSpentDetail.to_json())

# convert the object into a dict
time_spent_detail_dict = time_spent_detail_instance.to_dict()
# create an instance of TimeSpentDetail from a dict
time_spent_detail_from_dict = TimeSpentDetail.from_dict(time_spent_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


