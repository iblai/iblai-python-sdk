# PathwayEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**ended** | **datetime** |  | [optional] 
**active** | **bool** |  | 

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


