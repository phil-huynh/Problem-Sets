
def total_song_knowers(villagers, attendees):
    songs= {}
    all_songs = 0
    knows_all_songs = 0

    # Add each villager(key) to the songs dictionary with a [] value and exclude the minstrel
    for villager in range(villagers):
        songs[villager + 1] = []

    # Check every night to see if the minstrel is present
    for i, night in enumerate(attendees):

        # if the minstrel is present, add new song to all villagers present
        if 0 in night:
            all_songs += 1
            for person in songs:
                if person in night:
                    songs[person].append(i)

        # otherwise everyone jams and trades songs
        else:

            # get a list of all of the tunes people from tonight know with duplicates removed
            jam = {}
            for person in night:
                for tune in songs[person]:
                    jam[tune] = True
            jam = list(jam.keys())

            # update everyones known tunes
            for person in night:
                songs[person] = jam.copy()

    # for each villager check to see if they know all of the songs
    for villager in songs:
        if len(songs[villager]) == all_songs:
            knows_all_songs += 1
    return knows_all_songs


# Same idea, shorter code

def total_song_knowers(villagers, attendees):
    setlist, minstrel = 0, 0
    songs = {villager + 1 : [] for villager in range(villagers)}

    for i, night in enumerate(attendees):
        if minstrel in night:
            setlist += 1
            for person in night:
                if person != minstrel:
                    songs[person].append(i)
        else:
            jam = list({tune:True for tune in songs[person] for person in night}.keys())
            for person in night:
                songs[person] = jam.copy()

    bad_cats = filter(lambda a:len(a)==setlist, songs.values())
    return len(list(bad_cats))