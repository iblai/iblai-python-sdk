# CeleryHeartbeatFail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**CeleryHeartbeatFailStatusEnum**](CeleryHeartbeatFailStatusEnum.md) |  | 
**message** | **str** |  | 

## Example

```python
from iblai.models.celery_heartbeat_fail import CeleryHeartbeatFail

# TODO update the JSON string below
json = "{}"
# create an instance of CeleryHeartbeatFail from a JSON string
celery_heartbeat_fail_instance = CeleryHeartbeatFail.from_json(json)
# print the JSON string representation of the object
print(CeleryHeartbeatFail.to_json())

# convert the object into a dict
celery_heartbeat_fail_dict = celery_heartbeat_fail_instance.to_dict()
# create an instance of CeleryHeartbeatFail from a dict
celery_heartbeat_fail_from_dict = CeleryHeartbeatFail.from_dict(celery_heartbeat_fail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


