import urllib.parse
import urllib.request
import json

def get_onedrive_reflesh_token(refresh_token: str):

    apl_client_id= "4e55f9b5-c3e4-476f-96a9-1c002b84f90a"
    client_secret = "MGR8Q~NlJMWUeA1-uxFU_r_lE_KjTUCfLvpDucRQ"
    redirect_url = "http://localhost:4200/"

    url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    method = "POST"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    params = {
        "client_id": apl_client_id
        ,"redirect_uri": redirect_url
        ,"client_secret": client_secret
        ,"refresh_token": refresh_token
        ,"grant_type": "refresh_token"
    }

    encoded_param = urllib.parse.urlencode(params).encode()

    request = urllib.request.Request(url, data=encoded_param, method=method, headers=headers)
    with urllib.request.urlopen(request) as res:
        body = res.read()
        #print(body)
        dat = json.loads(body)
        print(dat)

if __name__ == '__main__':

    refresh_token = "aaaaaa"
    get_onedrive_reflesh_token(refresh_token)