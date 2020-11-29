import PySimpleGUI as sg
from logical import UseGitHubAPI
import webbrowser, os

use = UseGitHubAPI()

sg.theme('DarkBlue')
layout = [
    [
        sg.Text('User Name: '), sg.In(key='input', text_color='Black'), 
        sg.B('Search', key='search'),
        sg.B('view repositories', key='repositories', disabled=True)
    ],
    [
        sg.Multiline(key='print_info', size=(90, 30), text_color='Black', disabled=True),
    ],
    [
        sg.B('previous', key='previous', disabled=True),
        sg.B('go to profile', key='go', disabled=True),  
        sg.B('next', key='next', disabled=True),
        sg.B('git clone', key='clone', disabled=True, pad=(('300', '3'), (None)))

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
        window['clone'].update(disabled=True)

    
    if event == 'go':
        try:
            url = use.returnProfileLink()
            webbrowser.open(url)
        except:
            ...
            
    if event == 'repositories':
        repositoryNow = 0
        window['print_info'].update(use.returnRepositoryInfo(repositoryNow))
        window['previous'].update(disabled=False)
        window['next'].update(disabled=False)
        window['clone'].update(disabled=False)

        
        
    if event == 'next':
        repositoryNow +=1
        isrepository = use.returnRepositoryInfo(repositoryNow)
        if type(isrepository) == str:
            window['print_info'].update(isrepository)
        else:
            repositoryNow -=1
    
    if event == 'previous':
        repositoryNow -=1
        if repositoryNow>=0:
            isrepository = use.returnRepositoryInfo(repositoryNow)
            if type(isrepository) == str:
                window['print_info'].update(isrepository)
            else:
                repositoryNow +=1
        else:
            repositoryNow +=1

    if event == 'clone':
        clone_url = use.returnCloneLink()
        try:
            os.system(f'cd ~/ && git clone {clone_url}')
            sg.popup('Repository was cloned with success')
        except:
            sg.popup('Process gave wrong\nCheck if you have git installed on your computer')
         
window.close()