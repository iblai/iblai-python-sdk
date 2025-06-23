# WhatsappUserConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user** | **int** | edX user ID | [readonly] 
**phone_number** | **str** |  | 
**date_created** | **datetime** |  | [readonly] 
**last_modified** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.whatsapp_user_config import WhatsappUserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappUserConfig from a JSON string
whatsapp_user_config_instance = WhatsappUserConfig.from_json(json)
# print the JSON string representation of the object
print(WhatsappUserConfig.to_json())

# convert the object into a dict
whatsapp_user_config_dict = whatsapp_user_config_instance.to_dict()
# create an instance of WhatsappUserConfig from a dict
whatsapp_user_config_from_dict = WhatsappUserConfig.from_dict(whatsapp_user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


