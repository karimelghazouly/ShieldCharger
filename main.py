import ShieldManager
import DBManager
import websocket
import requests
import json
import calc
import GameCalculator

game_calculator = GameCalculator.calculations(100, 100)

def configuration():
    confResponse = requests.get("http://54.188.229.169:8080/api/config")
    return confResponse.json()

def makedecision(fixed_values, curtemp, currad):
    maxtemp = fixed_values['maxTemperature']
    mintemp = fixed_values['minTemperature']
    maxrad = fixed_values['maxRadiation']
    minrad = fixed_values['minRadiation']
    lifeloss, energygained = game_calculator.calc_if_off(currad ,minrad, maxrad, curtemp, mintemp, maxtemp)
    decision = game_calculator.make_decision_turn_on_shield(energygained, lifeloss)
    game_calculator.make_change(energygained, lifeloss, decision)

    if(decision):
        ShieldManager.team_shield_up(team_name,team_auth)
    else:
        ShieldManager.team_shield_down(team_name,team_auth)
        

fixed_values = configuration()
ws = websocket.create_connection('ws://54.188.229.169:8080/ws')
DB = DBManager.DBManager()
team_name = 'rejectedletters' 
team_auth = ShieldManager.register_team(team_name)                         

while True:
    # get data from web socket
    json_string = ws.recv()
    parsed_json = json.loads(json_string)
    data = parsed_json['readings']
    
    DB.insrt(data)
    makedecision(fixed_values, data['temperature'], data['radiation'])
    
    