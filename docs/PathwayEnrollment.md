# PathwayEnrollment


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

## Example

```python
from iblai.models.pathway_enrollment import PathwayEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of PathwayEnrollment from a JSON string
pathway_enrollment_instance = PathwayEnrollment.from_json(json)
# print the JSON string representation of the object
print(PathwayEnrollment.to_json())

# convert the object into a dict
pathway_enrollment_dict = pathway_enrollment_instance.to_dict()
# create an instance of PathwayEnrollment from a dict
pathway_enrollment_from_dict = PathwayEnrollment.from_dict(pathway_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


