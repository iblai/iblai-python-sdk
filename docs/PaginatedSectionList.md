# PaginatedSectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Section]**](Section.md) |  | 

## Example

```python
from iblai.models.paginated_section_list import PaginatedSectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSectionList from a JSON string
paginated_section_list_instance = PaginatedSectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSectionList.to_json())

# convert the object into a dict
paginated_section_list_dict = paginated_section_list_instance.to_dict()
# create an instance of PaginatedSectionList from a dict
paginated_section_list_from_dict = PaginatedSectionList.from_dict(paginated_section_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


