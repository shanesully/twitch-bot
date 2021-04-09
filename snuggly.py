import requests
import json
import os

oauth_url = os.environ['OAUTH_URL']
get_user_url = os.environ['GET_USER_URL']
get_user_query = 'query=' + os.environ['CHANNEL_NAME']
channel_name = '#' + os.environ['CHANNEL_NAME']

def get_access_token(client_id, client_secret, grant_type):

    request = oauth_url + '?' + 'client_id=' + client_id + '&' + 'client_secret=' + client_secret + '&' + 'grant_type=' + grant_type
    response = requests.post(request)

    access_token = response.json()['access_token']

    if response.ok and access_token:
        return access_token
    else:
        return "Could not get access token"

def check_user_stream_status(client_id, client_secret, grant_type):
    
    oauth_token = 'Bearer' + ' ' + get_access_token(client_id, client_secret, grant_type)

    get_user_headers = {'Authorization': oauth_token, 'client-id': client_id}
    get_user_request = get_user_url + '?' + get_user_query

    get_user_response = requests.get(get_user_request, headers=get_user_headers)
    get_user_response_json = get_user_response.json()

    is_live = get_user_response_json['data'][0]['is_live']
    display_name = get_user_response_json['data'][0]['display_name']

    if is_live:
        print("{} is live!".format(display_name))
    else:
        print("{} is not live".format(display_name))

def main():

    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']
    grant_type = os.environ['GRANT_TYPE']

    check_user_stream_status(client_id, client_secret, grant_type)

if __name__ == "__main__":
    main()