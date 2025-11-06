
def identify_conflicts(venue1_schedule, venue2_schedule):

    confict ={}
    for pair in venue1_schedule.keys() & venue2_schedule.keys():
        if (venue1_schedule[pair] == venue2_schedule[pair]):
            confict[pair] =(venue1_schedule[pair], venue2_schedule[pair])

        
    return confict



venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
# {"Stromae": "9:00 PM", "HARDY": "7:00 PM"}