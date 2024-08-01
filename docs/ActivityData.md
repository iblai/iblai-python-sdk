# ActivityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | edx Course Id | 
**name** | **str** | Course name | 
**course_start** | **str** | Course start date | 
**course_end** | **str** | Course end date | 
**average_time_invested** | **float** | Overall course average time invested (other students inclusive) | 
**time_invested** | **int** | Total time spent | 
**days_away** | **str** | Days from today the course has been accessed | 
**last_access_date** | **str** | When course was last accessed | 
**days_accessed** | **int** | Unique days course was accessed | 

## Example

```python
from iblai.models.activity_data import ActivityData

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityData from a JSON string
activity_data_instance = ActivityData.from_json(json)
# print the JSON string representation of the object
print(ActivityData.to_json())

# convert the object into a dict
activity_data_dict = activity_data_instance.to_dict()
# create an instance of ActivityData from a dict
activity_data_from_dict = ActivityData.from_dict(activity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


