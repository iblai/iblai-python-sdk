# WhatAppWebHook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | **List[Dict[str, object]]** |  | 

## Example

```python
from iblai.models.what_app_web_hook import WhatAppWebHook

# TODO update the JSON string below
json = "{}"
# create an instance of WhatAppWebHook from a JSON string
what_app_web_hook_instance = WhatAppWebHook.from_json(json)
# print the JSON string representation of the object
print(WhatAppWebHook.to_json())

# convert the object into a dict
what_app_web_hook_dict = what_app_web_hook_instance.to_dict()
# create an instance of WhatAppWebHook from a dict
what_app_web_hook_from_dict = WhatAppWebHook.from_dict(what_app_web_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


