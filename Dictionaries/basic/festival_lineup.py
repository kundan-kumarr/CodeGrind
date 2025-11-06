""""


"""

def get_artist_info(artist, festival_schedule):
    # festival_schedule.get(artist)
    #not_found_message = {"message": "Artist not found"}
    #return festival_schedule.get(artist, not_found_message)

    notFound = {'message': 'Artist not found'}
    return festival_schedule.get(artist, notFound) 




festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
