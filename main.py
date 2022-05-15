import PySimpleGUI as sg
from logical import UseGitHubAPI
import webbrowser, os

github_api = UseGitHubAPI()

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
        user_name = values['input'].replace(' ', '')
        github_api.user = user_name
        window['print_info'].update(github_api.get_profile_info())
        window['go'].update(disabled=False)
        window['repositories'].update(disabled=False)
        window['previous'].update(disabled=True)
        window['next'].update(disabled=True)
        window['clone'].update(disabled=True)

    
    if event == 'go':
        try:
            url = github_api.get_profile_url()
            webbrowser.open(url)
        except:
            ...
            
    if event == 'repositories':
        repository_now = 0
        window['print_info'].update(github_api.get_repository_info(repository_now))
        window['previous'].update(disabled=False)
        window['next'].update(disabled=False)
        window['clone'].update(disabled=False)

        
        
    if event == 'next':
        repository_now += 1
        is_repository = github_api.get_repository_info(repository_now)
        if isinstance(is_repository, str):
            window['print_info'].update(is_repository)
        else:
            repository_now -=1 
    
    if event == 'previous':
        repository_now -= 1
        if repository_now >= 0:
            is_repository = github_api.get_repository_info(repository_now)
            if isinstance(is_repository, str):
               window['print_info'].update(is_repository)
            else:
               repository_now +=1
        else:
            repository_now += 1

    if event == 'clone':
        clone_url = github_api.get_clone_url(repository_now)
        try:
            os.system(f'cd ~/ && git clone {clone_url}')
            sg.popup('Repository was cloned with success')
        except:
            sg.popup('Process gave wrong\nCheck if you have git installed on your computer')

window.close()