# PaginatedEmailPromptListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[EmailPromptList]**](EmailPromptList.md) |  | 

## Example

```python
from iblai.models.paginated_email_prompt_list_list import PaginatedEmailPromptListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEmailPromptListList from a JSON string
paginated_email_prompt_list_list_instance = PaginatedEmailPromptListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEmailPromptListList.to_json())

# convert the object into a dict
paginated_email_prompt_list_list_dict = paginated_email_prompt_list_list_instance.to_dict()
# create an instance of PaginatedEmailPromptListList from a dict
paginated_email_prompt_list_list_from_dict = PaginatedEmailPromptListList.from_dict(paginated_email_prompt_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


