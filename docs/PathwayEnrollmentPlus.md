# PathwayEnrollmentPlus

Includes metadata+

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**pathway_id** | **str** |  | [optional] 
**pathway_uuid** | **str** |  | [optional] 
**platform_key** | **str** |  | [optional] 
**org** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**created** | **datetime** | Date when enrollment began/activated | [optional] 
**ended** | **datetime** | Date when enrollment ended/deactivated | [readonly] 
**active** | **bool** | Whether the enrollment is active | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from iblai.models.pathway_enrollment_plus import PathwayEnrollmentPlus

# TODO update the JSON string below
json = "{}"
# create an instance of PathwayEnrollmentPlus from a JSON string
pathway_enrollment_plus_instance = PathwayEnrollmentPlus.from_json(json)
# print the JSON string representation of the object
print(PathwayEnrollmentPlus.to_json())

# convert the object into a dict
pathway_enrollment_plus_dict = pathway_enrollment_plus_instance.to_dict()
# create an instance of PathwayEnrollmentPlus from a dict
pathway_enrollment_plus_from_dict = PathwayEnrollmentPlus.from_dict(pathway_enrollment_plus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


