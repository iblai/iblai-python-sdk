# GradingPerUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | learner username | 
**full_name** | **str** | learner Name | 
**start_date** | **str** | Course enrollment date | 
**submissions** | **int** | Total assessment submissions | 
**last_active** | **str** | Last active time | 
**percent** | **float** | TStudent course grade | 

## Example

```python
from iblai.models.grading_per_user_data import GradingPerUserData

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPerUserData from a JSON string
grading_per_user_data_instance = GradingPerUserData.from_json(json)
# print the JSON string representation of the object
print(GradingPerUserData.to_json())

# convert the object into a dict
grading_per_user_data_dict = grading_per_user_data_instance.to_dict()
# create an instance of GradingPerUserData from a dict
grading_per_user_data_from_dict = GradingPerUserData.from_dict(grading_per_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


