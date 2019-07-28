import requests 

#Check Grafana is up
grafana = 'http://localhost:3000' 
response = requests.get(grafana)        # To execute get request 
if response.status_code == 200:
    print('Success!')
elif response.status_code != 200:
    print('Not Found.')

#Check Prometheus is up
prometheus = 'http://localhost:9090' 
response = requests.get(prometheus)        # To execute get request 
if response.status_code == 200:
    print('Success!')
elif response.status_code != 200:
    print('Not Found.')

