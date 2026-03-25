# EnrollmentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**started** | **datetime** |  | [optional] 
**ended** | **datetime** |  | [optional] 
**active** | **bool** |  | 

## Example

```python
from iblai.models.enrollment_info import EnrollmentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentInfo from a JSON string
enrollment_info_instance = EnrollmentInfo.from_json(json)
# print the JSON string representation of the object
print(EnrollmentInfo.to_json())

# convert the object into a dict
enrollment_info_dict = enrollment_info_instance.to_dict()
# create an instance of EnrollmentInfo from a dict
enrollment_info_from_dict = EnrollmentInfo.from_dict(enrollment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


