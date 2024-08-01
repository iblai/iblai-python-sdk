# EnrollmentsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | Edx Course ID | 
**name** | **str** | Course Name | 
**users** | **int** | Number of users | 
**percentage** | **float** | Percentage ... | 

## Example

```python
from iblai.models.enrollments_data import EnrollmentsData

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentsData from a JSON string
enrollments_data_instance = EnrollmentsData.from_json(json)
# print the JSON string representation of the object
print(EnrollmentsData.to_json())

# convert the object into a dict
enrollments_data_dict = enrollments_data_instance.to_dict()
# create an instance of EnrollmentsData from a dict
enrollments_data_from_dict = EnrollmentsData.from_dict(enrollments_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


