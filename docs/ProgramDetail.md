# ProgramDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **str** |  | 
**name** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**enrollment** | [**EnrollmentInfo**](EnrollmentInfo.md) |  | 
**completion** | [**ProgramCompletion**](ProgramCompletion.md) |  | [optional] 

## Example

```python
from iblai.models.program_detail import ProgramDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramDetail from a JSON string
program_detail_instance = ProgramDetail.from_json(json)
# print the JSON string representation of the object
print(ProgramDetail.to_json())

# convert the object into a dict
program_detail_dict = program_detail_instance.to_dict()
# create an instance of ProgramDetail from a dict
program_detail_from_dict = ProgramDetail.from_dict(program_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


