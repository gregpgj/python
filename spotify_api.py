import spotipy.util as util

username = '12159259511'
client_id = '8410d0c855f4425186303b8101144993'
client_secret = '66ec63f759314e84aeea36099bf0e716'
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-recently-played'

token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)