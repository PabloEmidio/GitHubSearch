import PySimpleGUI as sg
from logical import UseGitHubAPI
import webbrowser

use = UseGitHubAPI()

sg.theme('DarkBlue')
layout = [
    [
        sg.Text('User Name: '), sg.In(key='input', text_color='Black'), 
        sg.B('Search', key='search')
    ],
    [
        sg.Multiline(key='test', size=(65, 30), text_color='Black')
    ],
    [
        sg.B('go to profile', key='go', visible=False)
    ]]

window = sg.Window('GitHub Search', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'search':
        searching = values['input'].replace(' ', '')
        window['test'].update(use.takeInfo(searching))
        window['go'].update(visible=True)
    
    if event == 'go':
        url = use.returnProfileLink()
        webbrowser.open(url)

