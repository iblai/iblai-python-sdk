# PathwayEnrollmentRequest

Serializer for pathway enrollment request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID for enrollment | [optional] 
**username** | **str** | Username for enrollment | [optional] 
**pathway_id** | **str** | Pathway ID for enrollment | [optional] 
**pathway_uuid** | **str** | Pathway UUID for enrollment | [optional] 
**pathway_key** | **str** | Pathway key for enrollment | [optional] 
**slug** | **str** | Pathway slug for enrollment | [optional] 
**org** | **str** | Organization for the pathway | [optional] 
**platform_key** | **str** | Platform key for the pathway | [optional] 
**include_default_platform** | **bool** | Include enrollments from default platform | [optional] 
**include_metadata** | **bool** | Include metadata in the response | [optional] [default to True]
**active** | **bool** | Whether the enrollment should be active | [optional] [default to True]

## Example

```python
from iblai.models.pathway_enrollment_request import PathwayEnrollmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PathwayEnrollmentRequest from a JSON string
pathway_enrollment_request_instance = PathwayEnrollmentRequest.from_json(json)
# print the JSON string representation of the object
print(PathwayEnrollmentRequest.to_json())

# convert the object into a dict
pathway_enrollment_request_dict = pathway_enrollment_request_instance.to_dict()
# create an instance of PathwayEnrollmentRequest from a dict
pathway_enrollment_request_from_dict = PathwayEnrollmentRequest.from_dict(pathway_enrollment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


