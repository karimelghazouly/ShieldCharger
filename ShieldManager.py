import requests
import websocket
import json

server_url = 'http://54.188.229.169:8080/api'   
server_ws = 'ws://54.188.229.169:8080/ws'       


def register_team(team_name):
    url = server_url + "/join/" + team_name
    print('Server API URL: ' + url)
    payload = ''
    response = requests.post(url, data=payload)

    team_auth = response.text
    # print ('Team Authentication Code:' + team_auth )

    if response.status_code == 200:
        print ('Team \'' + team_name + '\' joined the game!')
        print (team_name + ' authentication Code: ' + team_auth)
    else:
        print ('Team \'' + team_name + '\' joining game Failed!')
        print ("HTTP Code: " + str(response.status_code) + " | Response: " + response.text)

    return team_auth


def team_shield_up(team_name, team_auth):
    url = server_url + '/shield/enable'
    auth_header = {'X-Auth-Token': team_auth}
    shield_up = requests.post(url, headers=auth_header)
    if shield_up.status_code == 200:
        print ('Server: Team: ' + team_name + ' Shield is UP!')
    else:
        print ('Server: Team: ' + team_name + ' Shield UP! request Failed!')
        print ("HTTP Code: " + str(shield_up.status_code) + " | Response: " + shield_up.text)


def team_shield_down(team_name, team_auth):
    url = server_url + '/shield/disable'
    auth_header = {'X-Auth-Token': team_auth}
    shield_down = requests.post(url, headers=auth_header)
    if shield_down.status_code == 200:
        print ('Server: Team: ' + team_name + ' Shield is DOWN!')
    else:
        print ('Server: Team: ' + team_name + ' Shield DOWN! request Failed!')
        print ("HTTP Code: " + str(shield_down.status_code) + " | Response: " + shield_down.text)

