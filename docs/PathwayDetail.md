# PathwayDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pathway_id** | **str** |  | 
**name** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**enrollment** | [**PathwayEnrollment**](PathwayEnrollment.md) |  | 
**completion** | [**PathwayCompletion**](PathwayCompletion.md) |  | [optional] 

## Example

```python
from iblai.models.pathway_detail import PathwayDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PathwayDetail from a JSON string
pathway_detail_instance = PathwayDetail.from_json(json)
# print the JSON string representation of the object
print(PathwayDetail.to_json())

# convert the object into a dict
pathway_detail_dict = pathway_detail_instance.to_dict()
# create an instance of PathwayDetail from a dict
pathway_detail_from_dict = PathwayDetail.from_dict(pathway_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


