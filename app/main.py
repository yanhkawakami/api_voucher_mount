from flask import Flask
from flask import jsonify
from flask import request
from src.define_amount import AmountRecency, AmountFrequency


app = Flask(__name__)


@app.route('/most_used_voucher', methods=['POST'])
def get_most_used_voucher_value():
    """
    Function that allows to get the most used
    voucher value.
    """
    try:
        # Transform request in json and get fields
        json = request.json
        country_code = json["country_code"]
        last_order_ts = json["last_order_ts"]
        first_order_ts = json["first_order_ts"]
        total_orders = json["total_orders"]
        segment_name = json["segment_name"]

        # Check if needed fields exists ans if method is working
        if country_code and last_order_ts and first_order_ts \
                and total_orders and segment_name:

            # Check if it's a recency case
            if segment_name == 'recency_segment':
                ar = AmountRecency(last_order_ts, first_order_ts)
                amount = ar.get_amount_by_recency(country_code, segment_name)
            # Check if it's a frequency case
            else:
                af = AmountFrequency(total_orders)
                amount = af.get_amount_by_frequency(country_code, segment_name)
            msg = {
                "voucher_amount": int(amount)
            }
            response = jsonify(msg)
            return response
        else:
            return showMessage()
    except Exception as e:
        print(e)


# Error Handle 404
@app.errorhandler(404)
def showMessage(error=None):
    """
    Function that returns when we have a 404
    error on endpoint
    """
    message = {
        'status': 404,
        'message': 'Not valid request'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
