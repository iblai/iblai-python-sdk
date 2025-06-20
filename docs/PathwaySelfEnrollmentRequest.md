# PathwaySelfEnrollmentRequest

Serializer for pathway self-enrollment request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID for self-enrollment | [optional] 
**username** | **str** | Username for self-enrollment | [optional] 
**pathway_id** | **str** | Pathway ID for self-enrollment | [optional] 
**pathway_key** | **str** | Pathway key for self-enrollment | [optional] 
**slug** | **str** | Pathway slug for self-enrollment | [optional] 
**org** | **str** | Organization for the pathway | [optional] 
**platform_key** | **str** | Platform key for the pathway | [optional] 
**active** | **bool** | Whether the enrollment should be active | [optional] [default to True]

## Example

```python
from iblai.models.pathway_self_enrollment_request import PathwaySelfEnrollmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PathwaySelfEnrollmentRequest from a JSON string
pathway_self_enrollment_request_instance = PathwaySelfEnrollmentRequest.from_json(json)
# print the JSON string representation of the object
print(PathwaySelfEnrollmentRequest.to_json())

# convert the object into a dict
pathway_self_enrollment_request_dict = pathway_self_enrollment_request_instance.to_dict()
# create an instance of PathwaySelfEnrollmentRequest from a dict
pathway_self_enrollment_request_from_dict = PathwaySelfEnrollmentRequest.from_dict(pathway_self_enrollment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


