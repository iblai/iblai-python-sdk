# HeygenMarketingVideoList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**pk** | **int** |  | [readonly] 
**generation_status** | **str** |  | [readonly] 

## Example

```python
from iblai.models.heygen_marketing_video_list import HeygenMarketingVideoList

# TODO update the JSON string below
json = "{}"
# create an instance of HeygenMarketingVideoList from a JSON string
heygen_marketing_video_list_instance = HeygenMarketingVideoList.from_json(json)
# print the JSON string representation of the object
print(HeygenMarketingVideoList.to_json())

# convert the object into a dict
heygen_marketing_video_list_dict = heygen_marketing_video_list_instance.to_dict()
# create an instance of HeygenMarketingVideoList from a dict
heygen_marketing_video_list_from_dict = HeygenMarketingVideoList.from_dict(heygen_marketing_video_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


