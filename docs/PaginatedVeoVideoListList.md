# PaginatedVeoVideoListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[VeoVideoList]**](VeoVideoList.md) |  | 

## Example

```python
from iblai.models.paginated_veo_video_list_list import PaginatedVeoVideoListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedVeoVideoListList from a JSON string
paginated_veo_video_list_list_instance = PaginatedVeoVideoListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedVeoVideoListList.to_json())

# convert the object into a dict
paginated_veo_video_list_list_dict = paginated_veo_video_list_list_instance.to_dict()
# create an instance of PaginatedVeoVideoListList from a dict
paginated_veo_video_list_list_from_dict = PaginatedVeoVideoListList.from_dict(paginated_veo_video_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


