# PaginatedGoogleAgentDetailList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GoogleAgentDetail]**](GoogleAgentDetail.md) |  | 

## Example

```python
from iblai.models.paginated_google_agent_detail_list import PaginatedGoogleAgentDetailList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGoogleAgentDetailList from a JSON string
paginated_google_agent_detail_list_instance = PaginatedGoogleAgentDetailList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGoogleAgentDetailList.to_json())

# convert the object into a dict
paginated_google_agent_detail_list_dict = paginated_google_agent_detail_list_instance.to_dict()
# create an instance of PaginatedGoogleAgentDetailList from a dict
paginated_google_agent_detail_list_from_dict = PaginatedGoogleAgentDetailList.from_dict(paginated_google_agent_detail_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


