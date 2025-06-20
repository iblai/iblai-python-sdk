# CampaignExclusion

Serializer for campaign exclusion requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** |  | [optional] 
**campaign_title** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from iblai.models.campaign_exclusion import CampaignExclusion

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignExclusion from a JSON string
campaign_exclusion_instance = CampaignExclusion.from_json(json)
# print the JSON string representation of the object
print(CampaignExclusion.to_json())

# convert the object into a dict
campaign_exclusion_dict = campaign_exclusion_instance.to_dict()
# create an instance of CampaignExclusion from a dict
campaign_exclusion_from_dict = CampaignExclusion.from_dict(campaign_exclusion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


