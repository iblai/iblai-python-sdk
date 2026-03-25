# UserChatPrivacySettings

Serializer for user chat privacy settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_privacy_mode** | [**ChatPrivacyModeEnum**](ChatPrivacyModeEnum.md) | User&#39;s global chat privacy preference  * &#x60;normal&#x60; - Normal * &#x60;anonymized&#x60; - Anonymized * &#x60;disabled&#x60; - Disabled | [optional] 
**chat_privacy_enabled** | **bool** | Whether chat privacy control is enabled for this platform | [readonly] 

## Example

```python
from iblai.models.user_chat_privacy_settings import UserChatPrivacySettings

# TODO update the JSON string below
json = "{}"
# create an instance of UserChatPrivacySettings from a JSON string
user_chat_privacy_settings_instance = UserChatPrivacySettings.from_json(json)
# print the JSON string representation of the object
print(UserChatPrivacySettings.to_json())

# convert the object into a dict
user_chat_privacy_settings_dict = user_chat_privacy_settings_instance.to_dict()
# create an instance of UserChatPrivacySettings from a dict
user_chat_privacy_settings_from_dict = UserChatPrivacySettings.from_dict(user_chat_privacy_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


