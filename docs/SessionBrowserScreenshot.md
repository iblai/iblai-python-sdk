# SessionBrowserScreenshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**session_id** | **str** |  | 
**format** | **str** |  | 
**ext** | **str** |  | 
**url** | **str** |  | 
**time** | **datetime** |  | 

## Example

```python
from iblai.models.session_browser_screenshot import SessionBrowserScreenshot

# TODO update the JSON string below
json = "{}"
# create an instance of SessionBrowserScreenshot from a JSON string
session_browser_screenshot_instance = SessionBrowserScreenshot.from_json(json)
# print the JSON string representation of the object
print(SessionBrowserScreenshot.to_json())

# convert the object into a dict
session_browser_screenshot_dict = session_browser_screenshot_instance.to_dict()
# create an instance of SessionBrowserScreenshot from a dict
session_browser_screenshot_from_dict = SessionBrowserScreenshot.from_dict(session_browser_screenshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


