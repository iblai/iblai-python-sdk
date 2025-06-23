# CampaignEnablement

Serializer for campaign enablement requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** |  | [optional] 
**campaign_title** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from iblai.models.campaign_enablement import CampaignEnablement

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignEnablement from a JSON string
campaign_enablement_instance = CampaignEnablement.from_json(json)
# print the JSON string representation of the object
print(CampaignEnablement.to_json())

# convert the object into a dict
campaign_enablement_dict = campaign_enablement_instance.to_dict()
# create an instance of CampaignEnablement from a dict
campaign_enablement_from_dict = CampaignEnablement.from_dict(campaign_enablement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


