import requests, json

class UseGitHubAPI:
    
    def _takeProfileInfo(self, user):
        url = f'https://api.github.com/users/{user}'
        try:
            with requests.get(url) as response:
                self._takenProfileJson = json.loads(response.text)
        except:
            ...
        
        
    def _selectProfileFields(self, info):
        self._selectedProfileFields = {
            'Name': info['name'],
            'Bio': info['bio'],
            'Email': info['email'],
            'Company': info['company'],
            'Blog': info['blog'],
            'Location': info['location'],
            'Type': info['type'],
            'Hireable': info['hireable'],
            'Created at': info['created_at'].replace('Z', '').replace('T', ' '),
            'Updated at': info['updated_at'].replace('Z', '').replace('T', ' '),
            'Followers': info['followers'],
            'Following': info['following'],
            'Public repositories': info['public_repos'],
            'public_gists': info['public_gists'],
            'Twitter': info['twitter_username'],
            'URL': info['html_url']}
    
    
    def returnProfileInfo(self, user=''):
        try:
            self._takeProfileInfo(user)
            self._selectProfileFields(self._takenProfileJson)
            self.readable = ''
            self.readable = self.turnReadable(self._selectedProfileFields)
            return self.readable
        except:
            return 'not found'
    
        
    def returnProfileLink(self):
        return self._selectedProfileFields['URL']
    
    
    def turnReadable(self, dictionary):
        self.turningReadable = ''
        for k, v in dictionary.items():
            if v == '':
                v = None
            self.turningReadable = self.turningReadable + f'{k}: {v} \n\n'     
        return self.turningReadable
    
    
    def _takeRepositoriesInfo(self):
        try:
            url = self._takenProfileJson['url'] + '/repos'
            with requests.get(url) as response:
                self._takenRepositoriesJson = json.loads(response.text)
            return True
        except:
            return False
            
    def _selectRepositorieFields(self, info, pos=0):
        if pos>len(info)-1:
            return False
        else:    
            info = info[pos]
            self._selectedRepositorieFields = {
                'Name': info['name'],
                'Description': info['description'],
                'Language': info['language'],
                'Private': info['private'],
                'URL': info['html_url'],
                'Default branch': info['default_branch'],
                'was it a fork': info['fork'],
                'Created at': info['created_at'].replace('Z', '').replace('T', ' '),
                'Updated at': info['updated_at'].replace('Z', '').replace('T', ' '),
                'Stargazers': info['stargazers_count'],
                'Watchers': info['watchers'],
                'Git url': info['git_url'],
                'SSH url': info['ssh_url'],
                'Clone url': info['clone_url']}
            return True
        

    def returnRepositorieInfo(self, pos):
        try:
            if self._takeRepositoriesInfo() and self._selectRepositorieFields(info=self._takenRepositoriesJson, pos=pos):
                self.readable = self.turnReadable(self._selectedRepositorieFields)
                return self.readable
            else:
                return False
        except:
            return False

