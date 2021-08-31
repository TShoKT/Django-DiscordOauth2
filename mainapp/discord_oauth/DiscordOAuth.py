from requests import Session
from decouple import config

client_id, client_secret = config("client_id", cast=str) , config("client_secret", cast=str)
auth_url_discord, redirect_uri = config("auth_url_discord", cast=str) , config("redirect_uri", cast=str)

default_icon_avatar = "https://cdn.discordapp.com/embed/avatars/0.png"

class AuthError(Exception):

  def __init__(self, msg) -> None:
    super().__init__(msg)

class Auth(Session):

  BASE, HEADERS = "https://discord.com/api/v9/", {'Content-Type': 'application/x-www-form-urlencoded'}

  def __init__(self, code=None,*args, **kwargs) -> None:
    
    self.__data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": redirect_uri,
    }
    
    self.__token = ""
    
    super().__init__(*args, **kwargs)
  
  def __exchange_code(self) -> str:

    if not self.__data['code']:
      raise AuthError("Code undefined, if you have AuthToken use from user or guilds method")
    response = self.post(self.BASE + "oauth2/token", data=self.__data, headers=self.HEADERS)
    if response.status_code == 200:
      self.__token = response.json()["access_token"]
      return self.__token
    raise AuthError(f"Failed to connect to discord API {response.json()}")
  
  @property
  def token(self):
    
    if not self.__token:
      self.__exchange_code()
    
    return self.__token
    

  def user(self, token=None) -> dict:
    if not token:
      try:
        token = self.token
      except AttributeError:
        token = self.__exchange_code()

    response =  self.get(self.BASE + "users/@me", headers={'Authorization': f'Bearer {token}'})
    if response.status_code == 200:
      return response.json()
    raise AuthError("Failed to connect to discord API")
    
  def guilds(self, token=None) -> list:
    if not token:
      token = self.token
    response = self.get(self.BASE + "users/@me/guilds", headers={'Authorization': f'Bearer {token}'})
    if response.status_code == 200:
      return response.json()
    raise AuthError("Failed to connect to discord API")

class User:

  def __init__(self, user : dict) -> None:
    self.__user = user
    for k , v in self.__user.items():
      try:
        setattr(self, k, v)
      except AttributeError:
        continue

  @property
  def premium_type(self):
    types = ["Does not have", "Nitro Classic", "Nitro"]
    try:
      return types[self.__user["premium_type"]]
    except KeyError:
      return None
  
  @property
  def avatar(self):
    return f"https://cdn.discordapp.com/avatars/{self.__user['id']}/{self.__user['avatar']}" if self.__user['avatar'] else default_icon_avatar


class Guilds:

  def __init__(self, guilds : list) -> None:
    self.__guilds = guilds

  def __iter__(self):
    return iter([Guild(guild) for guild in self.__guilds])

  def __repr__(self) -> str:
      return repr(self.__guilds)


class Guild:
  def __init__(self, guild : dict) -> None:
    self.__guild = guild
    for k, v in self.__guild.items():
      try:
        setattr(self, k , v)
      except AttributeError:
        continue

  def __repr__(self) -> str:
    return repr(self.__guild)

  @property
  def user_is_administrator(self):
    return self.__guild["permissions"] == '274877906943'
  
  @property
  def icon(self):
    return f"https://cdn.discordapp.com/icons/{self.__guild['id']}/{self.__guild['icon']}.png" if self.__guild['icon'] else default_icon_avatar
    

if __name__ == "__main__":
  print(client_id)