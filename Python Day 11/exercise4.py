# Extract the phone number from this dictionary

message = {
	'Body' : {
		'stkCallback': {
			'MerchantRequestID': '677-6442255-1',
			'CheckoutRequestID': 'ws_CO_110520202014057155',
			'ResultCode': 0,
			'ResultDesc': 'The service request is processed successfully.',
			'CallbackMetadata': {
				'Item': [{
					'Name': 'Amount',
					'Value': 1.0
				}, {
					'Name': 'MpesaReceiptNumber',
					'Value': 'OEB44R5U3U'
				}, {
					'Name': 'Balance'
				}, {
					'Name': 'TransactionDate',
					'Value': 20200511201419
				}, {
					'Name': 'PhoneNumber',
					'Value': 254794721438
				}] # list of dictionaries
			}
		}
	}
}

body = message['Body']
stkCallback = body['stkCallback']
CallbackMetadata = stkCallback['CallbackMetadata']
Item = CallbackMetadata['Item']
last_item = Item[4]
number = last_item['Value']


print(number)

# message = {
# 	'Body': {}
# }



