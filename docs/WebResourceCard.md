# WebResourceCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | 
**image_url** | **str** |  | 
**domain** | **str** |  | 
**site_name** | **str** |  | 

## Example

```python
from iblai.models.web_resource_card import WebResourceCard

# TODO update the JSON string below
json = "{}"
# create an instance of WebResourceCard from a JSON string
web_resource_card_instance = WebResourceCard.from_json(json)
# print the JSON string representation of the object
print(WebResourceCard.to_json())

# convert the object into a dict
web_resource_card_dict = web_resource_card_instance.to_dict()
# create an instance of WebResourceCard from a dict
web_resource_card_from_dict = WebResourceCard.from_dict(web_resource_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


