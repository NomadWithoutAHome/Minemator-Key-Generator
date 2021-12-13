import PySimpleGUI as sg
import requests

'''Mineimator Key Generator
   
   Purpose: I created this little tool just for fun, without any malacious intent. It is a very simple python script 
            that i created in a matter of seconds, you can choose to generate the serial completely free on there website at
            www.mineimator.com or throw them a couple bones to support there effort in making the program.
   
   Version: 0.1
   
   Update Log: 
              12/12/2021: Initial Release'''

headers = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Sec-GPC': '1',
    'Origin': 'https://www.mineimator.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.mineimator.com/upgrade',
    'Accept-Language': 'en-US,en;q=0.9',
}
data = {
  'frompage': 'true'
}

sg.theme('Dark Brown 4')

layout = [
    [sg.Text('Serial Key: '), sg.In(key='serial')],
    [sg.Button('Generate')]
]

window = sg.Window('Mineimator KeyGen (web version)', layout)

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    if event == 'Generate':
        response = requests.post('https://www.mineimator.com/php/upgrade/no-donate.php', headers=headers, data=data)
        window['serial'](response.text)
