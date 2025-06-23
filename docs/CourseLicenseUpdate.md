# CourseLicenseUpdate

Request serializer for CourseLicenseUpdateView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **int** | The ID of the license to update (required if external_id not provided) | [optional] 
**external_id** | **str** | External identifier of the license to update (required if license_id not provided) | [optional] 
**platform_key** | **str** | The platform key (not updatable) | [optional] 
**platform_org** | **str** | The platform organization (not updatable) | [optional] 
**course_id** | **str** | The course ID (not updatable) | [optional] 
**name** | **str** | Updated display name for the license | [optional] 
**count** | **int** | Updated number of seats purchased | [optional] 
**started** | **datetime** | Updated date when license should begin | [optional] 
**expired** | **datetime** | Updated date when license should expire | [optional] 
**active** | **bool** | Updated active status | [optional] 
**metadata** | **Dict[str, object]** | Updated additional license metadata | [optional] 
**source** | **str** | Updated source identifier | [optional] 
**transaction_id** | **str** | Transaction identifier for tracking | [optional] 
**change_type** | **str** | Type of change being made | [optional] [default to 'update']

## Example

```python
from iblai.models.course_license_update import CourseLicenseUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CourseLicenseUpdate from a JSON string
course_license_update_instance = CourseLicenseUpdate.from_json(json)
# print the JSON string representation of the object
print(CourseLicenseUpdate.to_json())

# convert the object into a dict
course_license_update_dict = course_license_update_instance.to_dict()
# create an instance of CourseLicenseUpdate from a dict
course_license_update_from_dict = CourseLicenseUpdate.from_dict(course_license_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


