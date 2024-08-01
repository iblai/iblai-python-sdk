# Enrollments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EnrollmentsData]**](EnrollmentsData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 
**meta** | [**OvertimeMeta**](OvertimeMeta.md) |  | [optional] 

## Example

```python
from iblai.models.enrollments import Enrollments

# TODO update the JSON string below
json = "{}"
# create an instance of Enrollments from a JSON string
enrollments_instance = Enrollments.from_json(json)
# print the JSON string representation of the object
print(Enrollments.to_json())

# convert the object into a dict
enrollments_dict = enrollments_instance.to_dict()
# create an instance of Enrollments from a dict
enrollments_from_dict = Enrollments.from_dict(enrollments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


