# PaginatedHeygenTemplateResponseSingleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[HeygenTemplateResponseSingle]**](HeygenTemplateResponseSingle.md) |  | 

## Example

```python
from iblai.models.paginated_heygen_template_response_single_list import PaginatedHeygenTemplateResponseSingleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedHeygenTemplateResponseSingleList from a JSON string
paginated_heygen_template_response_single_list_instance = PaginatedHeygenTemplateResponseSingleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedHeygenTemplateResponseSingleList.to_json())

# convert the object into a dict
paginated_heygen_template_response_single_list_dict = paginated_heygen_template_response_single_list_instance.to_dict()
# create an instance of PaginatedHeygenTemplateResponseSingleList from a dict
paginated_heygen_template_response_single_list_from_dict = PaginatedHeygenTemplateResponseSingleList.from_dict(paginated_heygen_template_response_single_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


