# Data Challenge - API Voucher Amount

## 😄 How it was solved

The idea was an API with one endpoint using POST method. In backend, I got the most used voucher amount by each segment with historical data (data.parquet) and using user input I to check in which segment of frequency or recency the user was. Based on this, I got user segment and filtered historical data to find the best voucher amount to return in response.

To create segments, I used PDF description but for some cases that was not described, I used 'N/A' to mark as invalid values.

## 🚀 Explaining repository and code

Repository is divided by app, env and test folders. 
* app: contains the main code and source codes
	* src/data
		* content: folder to save data (parquet sent by Delivery Hero team)
		* data_orchestration.py: load data and invoke data_transformation module to filter data
		* data_transform.py: do all data preparation (fill NaN values and create segments considering intervals described in PDF) and filter methods by country code, valid values (filter values that are not in frequency and recency interval described in home task) and return most used voucher amount by segment
		* user_data.py: treats user data to get recency and frequency of user
	* src:
		* define_amount.py: get amount by recency and frequency based on historical data (data.parquet) and input from API to return best voucher amount for each user
		* flask_instance.py: flask instance to run a localhost server
	* main.py: declare route and implements logic to invoke classes for recency or frequency cases
	* tests: folder with all unit tests
* env: contains environment files (not used in this project - could be used to configurate flask environment)

For unit testing, I tested all modules only considering success cases (I thought that would be fine for home task). I had problems to deal with integration testing using Flask to check if API was running fine. So I didn't missed out time trying to do it, but I think that would be a relevant test.

## ☕ How to execute the code:

1. Open Docker Desktop
2. Build image while in root directory of project (/data_challenge) with command "docker build . -t dh_image"
3. Run docker conatainer with image built using command "docker run -it -p 5000:5000 dh_image"
4. Use Insomnia/Postman to call endpoint (http://localhost:5000/most_used_voucher - host can be 127.0.0.1:5000 instead localhost:5000) to get the amount voucher value desired

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