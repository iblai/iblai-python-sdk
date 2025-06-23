# PatchedWhatsappConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**bot** | **int** |  | [optional] [readonly] 
**phone_number_id** | **str** |  | [optional] 
**application_secret** | **str** |  | [optional] 
**webhook_verification_token** | **str** |  | [optional] 
**access_token** | **str** | Access token to the bot. This can also be a temporary access token. | [optional] 

## Example

```python
from iblai.models.patched_whatsapp_config import PatchedWhatsappConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedWhatsappConfig from a JSON string
patched_whatsapp_config_instance = PatchedWhatsappConfig.from_json(json)
# print the JSON string representation of the object
print(PatchedWhatsappConfig.to_json())

# convert the object into a dict
patched_whatsapp_config_dict = patched_whatsapp_config_instance.to_dict()
# create an instance of PatchedWhatsappConfig from a dict
patched_whatsapp_config_from_dict = PatchedWhatsappConfig.from_dict(patched_whatsapp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


