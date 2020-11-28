import requests
import json

class UseGitHubAPI:
    
    def takeInfo(self, user):
        url = f'https://api.github.com/users/{user}'
        try:
            with requests.get(url) as response:
                self._takedJson = json.loads(response.text)
            self.selectFields(self._takedJson)
            self.readable = ''
            for k, v in self.selectedFields.items():
                if v == '':
                    v = None
                self.readable = self.readable + f'{k}: {v} \n\n'     
            return self.readable
        except:
            return 'not found'
        
    def selectFields(self, info):
        self.selectedFields = {
            'Name': info['name'],
            'Bio': info['bio'],
            'Email': info['email'],
            'Company': info['company'],
            'Blog': info['blog'],
            'Location': info['location'],
            'Type': info['type'],
            'Hireable': info['hireable'],
            'Created at': info['created_at'],
            'Updated at': info['updated_at'],
            'Followers': info['followers'],
            'Following': info['following'],
            'Public repositories': info['public_repos'],
            'public_gists': info['public_gists'],
            'Twitter': info['twitter_username'],
            'URL': info['html_url']}
        
        
    def returnProfileLink(self):
        return self.selectedFields['URL']
