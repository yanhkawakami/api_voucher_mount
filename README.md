# Data Challenge - API Voucher Amount

## ☕ How to execute the code:

1. Execute app/main.py to establish local server
2. Use Insomnia/Postman to call endpoint (http://localhost:5000/most_used_voucher) to get the amount value

```
{
  "customer_id": 123, // customer id
	 "country_code": "Peru",  // customer’s country
	 "last_order_ts": "2018-05-03 00:00:00",  // ts of the last order placed by a customer
	 “first_order_ts”: "2017-05-03 00:00:00", // ts of the first order placed by a customer
	 "total_orders": 15, // total orders placed by a customer
	 "segment_name": "recency_segment" // which segment a customer belongs to
}

```