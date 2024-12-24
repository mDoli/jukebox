#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import config
import beeper
import data_management
from datetime import datetime

print("Welcome in spotify player")
now = datetime.now()
print("It is ", now.strftime("%Y-%m-%d %H:%M:%S"))

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                                       client_secret=config.CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id=reader.read()[0]
            print("Card Value is:", id)
            sp.transfer_playback(device_id=config.DEVICE_ID, force_play=False)
            
            # DONT include the quotation marks around the card's ID value, just paste the number
            if (id==config.master_card): # master-card-for-programming
                # sp.start_playback(device_id=config.DEVICE_ID, context_uri='spotify:album:0JGOiO34nwfUdDrD612dOp')
                # continue
                # 1. Read master card
                # 2. Play a song (or album?) from mobile/desktop
                    # 2.1. Check if result["context"]["uri"] exists and contains album, if yes save it
                # 3. Read a card you want to program
                # 4. Save it in json
                result = sp.current_playback()
                # print("Currently playing:", result)
                # print("Context:", result["context"])
                # print("Item:", result["item"])
                itemPlaying = result["item"]
                if not itemPlaying:
                    print("Nothing is playing!")
                    continue
                # print("Context uri: ", result["context"]["uri"])
                # print("Item uri: ", result["item"]["uri"])
                context=result["context"]
                uri = context["uri"] if context and context["type"]=="album" else result["item"]["uri"]
                print("uri: ", uri)
                name = result["item"]["album"]["name"] if ("album" in uri) else result["item"]["name"]
                print("Tap your card to save " + name + "...")
                id=reader.read()[0]
                if (id==config.master_card):
                    print("Master card is not to programm, canceling")
                    # beeper.beep()
                    # beeper.beep()
                    sleep(2)
                    continue
                print("Card Value is:", id)
                # beeper.beep()
                data_management.save_to_file(config.filename, id, uri)
                print("Saved:", name)
                sp.start_playback(device_id=config.DEVICE_ID, uris=[ config.jain_alright_song_uri ])
                
                sleep(2)
            
            else:
                uri = data_management.get_uri(config.filename, id)
                print("found uri:", uri)
                if "track" in uri:
                    sp.start_playback(device_id=config.DEVICE_ID, uris=[ uri ])
                elif "album" in uri:
                    sp.start_playback(device_id=config.DEVICE_ID, context_uri=uri)
                else:
                    print("No song assigned to card")
                sleep(2)
             # DONT edit here. Only edit the config.py file
            #elif id in config.SONGS.keys():

                # playing a song
            #    sp.start_playback(device_id=config.DEVICE_ID, uris=[ config.SONGS[id] ])
            #    sleep(2)

            #elif id in config.ALBUMS.keys():

                # playing an album
            #   sp.start_playback(device_id=config.DEVICE_ID, context_uri= config.ALBUMS[id])
            #    sleep(2)
            

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()