import requests
from werkzeug.exceptions import NotFound, HTTPException

from const import PROFILE_URL, USER_REPOSITORIES_URL


class UseGitHubAPI:
   def __init__(self, user: str = ''):
      self.__user = user

   @property
   def user(self) -> str:
      return self.__user
   
   @user.setter
   def user(self, username: str):
      self.__user = username

   @classmethod
   def __get_profile_info(cls, user: str) -> dict:
      try:
         with requests.get(PROFILE_URL.format(user)) as response:
            if response.status_code == 404:
               raise NotFound('Resource was not found')
            return cls.__select_profile_fields(response.json())
      except NotFound as err:
         raise err
      except Exception:
         raise HTTPException('Operation failed')

   @staticmethod
   def __select_profile_fields(info: dict) -> dict:
      selected_profile_fields = {
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
         'URL': info['html_url']
      }
      return selected_profile_fields

   def get_profile_info(self):
      try:
         profile_infos = self.__get_profile_info(self.user)
         return self.to_string(profile_infos)
      except Exception as err:
         return str(err)


   def get_profile_url(self):
      profile_infos = self.__get_profile_info(self.user)
      return profile_infos['URL']

   @staticmethod
   def to_string(infos: dict):
      readable = ''
      for k, v in infos.items():
         readable += f'{k}: {v or None} \n\n'
      return readable

   def __get_repositories_info(self, pos: int = 0) -> dict or None:
      try:
         url = USER_REPOSITORIES_URL.format(self.user)
         with requests.get(url) as response:
            if response.status_code == 404:
               raise NotFound('Resource was not found')
            return self.__select_repository_fields(response.json(), pos)
      except NotFound as err:
         raise err
      except Exception as err:
         print(err)
         raise HTTPException('Operation failed')
   
   @staticmethod
   def __select_repository_fields(infos: dict, pos: int = 0) -> dict or None:
      if pos > (len(infos) - 1):
         return None
      else:    
         info = infos[pos]
         selected_repository_fields = {
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
            'Clone url': info['clone_url']
         }
      return selected_repository_fields


   def get_repository_info(self, pos):
      try:
         get_repositories_info = self.__get_repositories_info(pos)
         return self.to_string(get_repositories_info)
      except Exception as err:
         return str(err)
         

   def get_clone_url(self, pos):
      get_repositories_info = self.__get_repositories_info(pos)
      return get_repositories_info['Clone url']
