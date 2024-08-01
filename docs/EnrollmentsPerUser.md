# EnrollmentsPerUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EnrollmentsPerUserData]**](EnrollmentsPerUserData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from iblai.models.enrollments_per_user import EnrollmentsPerUser

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentsPerUser from a JSON string
enrollments_per_user_instance = EnrollmentsPerUser.from_json(json)
# print the JSON string representation of the object
print(EnrollmentsPerUser.to_json())

# convert the object into a dict
enrollments_per_user_dict = enrollments_per_user_instance.to_dict()
# create an instance of EnrollmentsPerUser from a dict
enrollments_per_user_from_dict = EnrollmentsPerUser.from_dict(enrollments_per_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


