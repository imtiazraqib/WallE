# --------------------------------------------------------------------------------------------------------
# WallE - A Mastodon Bot
# Host Instance - botsin.space
# March 4, 2019
# ------------------------------------------
# Authors: Imtiaz Raqib
# --------------------------------------------------------------------------------------------------------

# IMPORTS ----------------------------------------------------
from mastodon import Mastodon
# ------------------------------------------------------------

def soccerToot():

    host_instance = 'https://botsin.space'
    
    #FIX ACCESS TOKEN
    token = ''
    
    mastodon = Mastodon(token, host_instance)

    mastodon.status_post("Hello everyone, I am testing my connection!")


soccerToot()

    