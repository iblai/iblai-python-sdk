# PaginatedHeygenMarketingVideoListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[HeygenMarketingVideoList]**](HeygenMarketingVideoList.md) |  | 

## Example

```python
from iblai.models.paginated_heygen_marketing_video_list_list import PaginatedHeygenMarketingVideoListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedHeygenMarketingVideoListList from a JSON string
paginated_heygen_marketing_video_list_list_instance = PaginatedHeygenMarketingVideoListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedHeygenMarketingVideoListList.to_json())

# convert the object into a dict
paginated_heygen_marketing_video_list_list_dict = paginated_heygen_marketing_video_list_list_instance.to_dict()
# create an instance of PaginatedHeygenMarketingVideoListList from a dict
paginated_heygen_marketing_video_list_list_from_dict = PaginatedHeygenMarketingVideoListList.from_dict(paginated_heygen_marketing_video_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


