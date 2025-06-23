# ProgramEnrollmentPlus

Includes metadata+

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**program_id** | **str** |  | [optional] 
**program_key** | **str** |  | [optional] 
**platform_key** | **str** |  | [optional] 
**org** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**created** | **datetime** | Date when enrollment began/activated | [optional] 
**started** | **datetime** | Date when enrollment started | [optional] 
**ended** | **datetime** | Date when enrollment ended/deactivated | [readonly] 
**expired** | **datetime** | Date when enrollment expires (null, if not expiring) | [optional] 
**active** | **bool** | Whether the enrollment is active | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from iblai.models.program_enrollment_plus import ProgramEnrollmentPlus

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramEnrollmentPlus from a JSON string
program_enrollment_plus_instance = ProgramEnrollmentPlus.from_json(json)
# print the JSON string representation of the object
print(ProgramEnrollmentPlus.to_json())

# convert the object into a dict
program_enrollment_plus_dict = program_enrollment_plus_instance.to_dict()
# create an instance of ProgramEnrollmentPlus from a dict
program_enrollment_plus_from_dict = ProgramEnrollmentPlus.from_dict(program_enrollment_plus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


