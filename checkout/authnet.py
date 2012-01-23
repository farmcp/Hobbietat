from ecomstore import settings
import httplib
import urllib

def do_auth_capture(amount='0.00', card_num=None, exp_date=None, card_cvv=None,bill_name=None,bill_address=None,bill_city=None, bill_state=None,bill_zip=None,bill_country=None,email=None,phone=None,ship_name=None,ship_address=None,ship_city=None,ship_state=None,ship_zip=None,ship_country=None):
    delimiter = '|'
    raw_params = {
        'x_login':settings.AUTHNET_LOGIN,
        'x_tran_key':settings.AUTHNET_KEY,
        'x_type':'AUTH_CAPTURE',
        'x_amount':amount,
        'x_version':'3.1',
        'x_card_num':card_num,
        'x_exp_date':exp_date,
        'x_delim_char':delimiter,
        'x_relay_response':'FALSE',
        'x_delim_data':'TRUE',
        'x_card_code':card_cvv,
        'x_first_name':bill_name,
        'x_address':bill_address,
        'x_city':bill_city,
        'x_state':bill_state,
        'x_zip':bill_zip,
        'x_country':bill_country,
        'x_email':email,
        'x_phone':phone,
        'x_ship_to_first_name':ship_name,
        'x_ship_to_address':ship_address,
        'x_ship_to_city':ship_city,
        'x_ship_to_state':ship_state,
        'x_ship_to_zip':ship_zip,
        'x_ship_to_country':ship_country
        }

    params = urllib.urlencode(raw_params)
    headers = {'content-type':'application/x-www-form-urlencoded',
               'content-length':len(params)}

    post_url = settings.AUTHNET_POST_URL
    post_path = settings.AUTHNET_POST_PATH
    cn = httplib.HTTPSConnection(post_url,httplib.HTTPS_PORT)
    cn.request('POST',post_path, params, headers)
    return cn.getresponse().read().split(delimiter)
