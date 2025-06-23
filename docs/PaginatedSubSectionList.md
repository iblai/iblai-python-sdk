# PaginatedSubSectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SubSection]**](SubSection.md) |  | 

## Example

```python
from iblai.models.paginated_sub_section_list import PaginatedSubSectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSubSectionList from a JSON string
paginated_sub_section_list_instance = PaginatedSubSectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSubSectionList.to_json())

# convert the object into a dict
paginated_sub_section_list_dict = paginated_sub_section_list_instance.to_dict()
# create an instance of PaginatedSubSectionList from a dict
paginated_sub_section_list_from_dict = PaginatedSubSectionList.from_dict(paginated_sub_section_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


