def total_song_knowers(num_villagers, attendees_lists):
    songlists= {}
    all_songs = 0
    knows_all_songs = 0
    for villager in range(num_villagers):
        songlists[villager + 1] = []
    for i, night in enumerate(attendees_lists):
        if 0 in night:
            all_songs += 1
            for person in songlists:
                if person in night:
                    songlists[person].append(i)
        else:
            jam_session = {}
            for person in night:
                for tune in songlists[person]:
                    jam_session[tune] = True
            jam_session = list(jam_session.keys())
            for person in night:
                songlists[person] = jam_session.copy()

    for villager in songlists:
        if len(songlists[villager]) == all_songs:
            knows_all_songs += 1
    return knows_all_songs