
# Edit the Spotify IDs and CLIENT_Secret below
DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca"
CLIENT_ID="c680d4b148af42ed87d91522cc3dc7aa"
CLIENT_SECRET="8963846d27dd41769528989c81986b93"

# File with your data
filename = "data.json"

# Master card for programming
master_card = 841041120746

jain_alright_song_uri='spotify:track:44ahv3Zj4FOJoy8gJLZF9B'
parostatek_song_uri='spotify:track:1OzlBug7c2LKPvIoMkuQhe'

# Add songs below if you want one RFID to play one song
SONGS = {
    # Format:
    #   RFID-CARDVALUE: 'uris_Value'
    151942008639: 'spotify:track:2vSLxBSZoK0eha4AuhZlXV',
    841041120746: 'spotify:track:4PTG3Z6ehGkBFwjybzWkR8',
}

# Add albums below if you want one RFID to play an album
ALBUMS = {
    # Format:
    #   RFID-CARDVALUE: 'context_uri_value',
    865202068078: 'spotify:album:0JGOiO34nwfUdDrD612dOp',
    246777109145: 'spotify:album:6eUW0wxWtzkFdaEFsTJto6',
}
