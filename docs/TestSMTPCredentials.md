# TestSMTPCredentials

Serializer for testing SMTP credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smtp_host** | **str** | SMTP server hostname | 
**smtp_port** | **int** | SMTP server port | 
**smtp_username** | **str** | SMTP username | 
**smtp_password** | **str** | SMTP password | 
**use_tls** | **bool** | Use TLS encryption | [optional] [default to True]
**use_ssl** | **bool** | Use SSL encryption | [optional] [default to False]
**test_email** | **str** | Email address to send test email to | 
**from_email** | **str** | From email address (optional) | [optional] 

## Example

```python
from iblai.models.test_smtp_credentials import TestSMTPCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of TestSMTPCredentials from a JSON string
test_smtp_credentials_instance = TestSMTPCredentials.from_json(json)
# print the JSON string representation of the object
print(TestSMTPCredentials.to_json())

# convert the object into a dict
test_smtp_credentials_dict = test_smtp_credentials_instance.to_dict()
# create an instance of TestSMTPCredentials from a dict
test_smtp_credentials_from_dict = TestSMTPCredentials.from_dict(test_smtp_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


