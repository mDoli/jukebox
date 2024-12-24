import json
import config

def save_to_file(filename, key, value):
    """
    Writes a song or album data to a JSON file.
    
    Args:
        filename: The name of the file to write to. Recommended to define it in config.
        key: The RFID card value (key) for the song/album.
        value: The Spotify URI (value) for the song/album.
    """
    try:
        # Read existing data
        with open(filename, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        # Create a new directory if the file doesn't exist
        data = {}
        
    key_str = str(key)
    
    # Add the new entry based on the key type (songs or albums)
    data[key_str] = value
    # Write the updated data back to the file
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def read_from_file(filename):
    """
    Reads a dictionary containing song/album data from a JSON file.
    
    Args:
        filename: The name of the file to read from. It is recommended to use name from config.
        
    Returns:
        A dictionary containing song and album data, or an empty dictionary if the file doesn't exist.
    """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def get_uri(filename, rfid_key):
    """
    Retrieves the Spotify URI for a sing/album vased on the RFID key-value
    
    Args:
        filename: The name of the data file.
        rfid_key: The RFID card value (key) for the song/album.
        
    Returns:
        The Spotify URI (value) for the song/album, or a default song if not found.
    """
    
    # Read the data from the file
    data = read_from_file(filename)
    
    # Convert the RFID key to a string for dictionary lookup (needed?)
    rfid_key_str = str(rfid_key)
    
    # Check if the key exists in the dictionary
    if rfid_key_str in data:
        return data[rfid_key_str]
    
    
    # Key not found in either dictionary
    return config.parostatek_song_uri # return Parostatkiem or Never gonna give you up
