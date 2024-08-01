# EnrollmentsPerUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | learner username | 
**full_name** | **str** | learner Name | 
**email** | **str** | Email | 
**timestamp** | **str** | Course start date | 

## Example

```python
from iblai.models.enrollments_per_user_data import EnrollmentsPerUserData

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentsPerUserData from a JSON string
enrollments_per_user_data_instance = EnrollmentsPerUserData.from_json(json)
# print the JSON string representation of the object
print(EnrollmentsPerUserData.to_json())

# convert the object into a dict
enrollments_per_user_data_dict = enrollments_per_user_data_instance.to_dict()
# create an instance of EnrollmentsPerUserData from a dict
enrollments_per_user_data_from_dict = EnrollmentsPerUserData.from_dict(enrollments_per_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


