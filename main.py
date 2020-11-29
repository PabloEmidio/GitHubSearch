import PySimpleGUI as sg
from logical import UseGitHubAPI
import webbrowser

use = UseGitHubAPI()

sg.theme('DarkBlue')
layout = [
    [
        sg.Text('User Name: '), sg.In(key='input', text_color='Black'), 
        sg.B('Search', key='search'),
        sg.B('view repositories', key='repositories', disabled=True)
    ],
    [
        sg.Multiline(key='print_info', size=(90, 30), text_color='Black'),
    ],
    [
        sg.B('previous', key='previous', disabled=True),
        sg.B('go to profile', key='go', disabled=True),  
        sg.B('next', key='next', disabled=True)
    ]]

window = sg.Window('GitHub Search', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'search':
        searching = values['input'].replace(' ', '')
        window['print_info'].update(use.returnProfileInfo(searching))
        window['go'].update(disabled=False)
        window['repositories'].update(disabled=False)
        window['previous'].update(disabled=True)
        window['next'].update(disabled=True)
    
    if event == 'go':
        try:
            url = use.returnProfileLink()
            webbrowser.open(url)
        except:
            ...
            
    if event == 'repositories':
        repositorieNow = 0
        window['print_info'].update(use.returnRepositorieInfo(repositorieNow))
        window['previous'].update(disabled=False)
        window['next'].update(disabled=False)
        
        
    if event == 'next':
        repositorieNow +=1
        print(f'in this next is {repositorieNow}')
        isrepositorie = use.returnRepositorieInfo(repositorieNow)
        if type(isrepositorie) == str:
            window['print_info'].update(isrepositorie)
        else:
            repositorieNow -=1
            print(f'gave wong in this next: {repositorieNow}')
    
    if event == 'previous':
        repositorieNow -=1
        print(f'in this previus is {repositorieNow}')
        if repositorieNow>0:
            isrepositorie = use.returnRepositorieInfo(repositorieNow)
            if type(isrepositorie) == str:
                window['print_info'].update(isrepositorie)
            else:
                repositorieNow +=1
                print(f'gave wong in this next: {repositorieNow}')

        else:
            repositorieNow +=1
            print(f'gave wong in this next: {repositorieNow}')


