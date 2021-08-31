from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import redirect
from mainapp.discord_oauth.DiscordOAuth import *

# Create your views here.


def null(request: HttpRequest):
  return redirect("home")


def home(request: HttpRequest):
  if request.method == "POST":
    try:
      del request.session["access_token"]
    except KeyError:
      pass
    
  return render(request, "home.html", context={"auth_url" : auth_url_discord})

def auth(request: HttpRequest):
  code = request.GET.get("code")

  if code:# if code is valid
    OAuth = Auth(code=code)
    request.session["access_token"] = OAuth.token

  else:
    access_token = request.session.get("access_token")
    if not access_token:#if token is not exists and not valid
      return redirect(auth_url_discord)# redirect to discord

  return redirect("user")


def user(request: HttpRequest):
  access_token = request.session.get("access_token")
  if access_token:#if token is valid
    OAuth = Auth()
    try:
      context = {
        "user" : User(OAuth.user(access_token)),
        "guilds" : Guilds(OAuth.guilds(access_token)),
      }
    except AuthError:
      return redirect(auth_url_discord)

  else:
    url  = request.build_absolute_uri().split("/")
    url.pop()
    return redirect("/".join([i for i in url]))

  return render(request, "user.html", context=context)

