# InvoiceReportResponse

Complete invoice report response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**Entity**](Entity.md) |  | 
**billing_period** | [**BillingPeriod**](BillingPeriod.md) |  | 
**summary** | [**Summary**](Summary.md) |  | 
**breakdown** | [**Breakdown**](Breakdown.md) |  | [optional] 

## Example

```python
from iblai.models.invoice_report_response import InvoiceReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReportResponse from a JSON string
invoice_report_response_instance = InvoiceReportResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceReportResponse.to_json())

# convert the object into a dict
invoice_report_response_dict = invoice_report_response_instance.to_dict()
# create an instance of InvoiceReportResponse from a dict
invoice_report_response_from_dict = InvoiceReportResponse.from_dict(invoice_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


