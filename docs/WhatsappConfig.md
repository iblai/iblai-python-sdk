# WhatsappConfig


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
from iblai.models.whatsapp_config import WhatsappConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappConfig from a JSON string
whatsapp_config_instance = WhatsappConfig.from_json(json)
# print the JSON string representation of the object
print(WhatsappConfig.to_json())

# convert the object into a dict
whatsapp_config_dict = whatsapp_config_instance.to_dict()
# create an instance of WhatsappConfig from a dict
whatsapp_config_from_dict = WhatsappConfig.from_dict(whatsapp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


