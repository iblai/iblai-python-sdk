# TimeDetailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_time** | **float** | Average time spent | 
**display_name** | **str** | Chapter name | 
**id** | **str** | Chapter Id | 
**children** | [**List[TimeDetailChild]**](TimeDetailChild.md) |  | [optional] 
**total_time** | **int** | Total time spent | [optional] 
**total_users** | **int** | Total users who accessed the chapter | [optional] 

## Example

```python
from iblai.models.time_detail_data import TimeDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of TimeDetailData from a JSON string
time_detail_data_instance = TimeDetailData.from_json(json)
# print the JSON string representation of the object
print(TimeDetailData.to_json())

# convert the object into a dict
time_detail_data_dict = time_detail_data_instance.to_dict()
# create an instance of TimeDetailData from a dict
time_detail_data_from_dict = TimeDetailData.from_dict(time_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


