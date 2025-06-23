# ProgramSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_list** | [**List[ProgramCoursePosition]**](ProgramCoursePosition.md) |  | 
**program_id** | **str** | A unique program ID identifiable by edX. | 
**program_key** | **str** |  | [readonly] 
**name** | **str** | The verbose name of the program. | [optional] 
**enabled** | **bool** | Select if this program should be enabled. | [optional] 
**slug** | **str** | An additional unique slug field. (Optional) | [optional] 
**org** | **str** |  | [optional] 
**platform_key** | **str** |  | [readonly] 
**program_type** | **str** |  | [readonly] 
**data** | **object** | Metadata | [optional] 

## Example

```python
from iblai.models.program_search import ProgramSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramSearch from a JSON string
program_search_instance = ProgramSearch.from_json(json)
# print the JSON string representation of the object
print(ProgramSearch.to_json())

# convert the object into a dict
program_search_dict = program_search_instance.to_dict()
# create an instance of ProgramSearch from a dict
program_search_from_dict = ProgramSearch.from_dict(program_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


