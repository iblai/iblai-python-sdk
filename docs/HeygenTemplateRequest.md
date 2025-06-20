# HeygenTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | 
**preview_image_url** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from iblai.models.heygen_template_request import HeygenTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HeygenTemplateRequest from a JSON string
heygen_template_request_instance = HeygenTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(HeygenTemplateRequest.to_json())

# convert the object into a dict
heygen_template_request_dict = heygen_template_request_instance.to_dict()
# create an instance of HeygenTemplateRequest from a dict
heygen_template_request_from_dict = HeygenTemplateRequest.from_dict(heygen_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


