#!/usr/bin/env python

"""A series of asserts to verify data quality."""
import json
import re

expected_ep_keys = [
    "title",
    "season",
    "episode",
    "release_date",
    "directors",
    "writers",
    "description",
    "disneyplus_id",
    "simpsonsworld_id",
    "good",
    "guest_stars",
]

print("loading file...")

with open("simpsons_data.json", "r") as f:
    all_json = json.load(f)
    all_episodes = all_json["episodes"]

    # EPISODE QA #

    print("QAing episodes...")

    for episode in all_episodes:
        # Should have expected keys
        # Debug print
        # print(f"#{episode['season']} - #{episode['episode']}")
        for key in expected_ep_keys:
            assert key in episode
        assert len(expected_ep_keys) == len(episode.keys())

        # Title should be a string
        assert isinstance(episode["title"], str)
        assert len(episode["title"]) > 0

        # Season should be an int
        assert isinstance(episode["season"], int)
        # assert episode['season'] < 50

        # Episode should be an int
        assert isinstance(episode["episode"], int)
        # assert episode['episode'] < 50

        # Description should be a string
        assert isinstance(episode["description"], str)

        # Release date should be a YYYY-MM-DD string if set
        if episode["release_date"] is not None:
            assert isinstance(episode["release_date"], str)
            assert re.match(r"\d{4}-\d{2}-\d{2}", episode["release_date"])

        # Simpsonsworld ID should be a str if set
        if episode["disneyplus_id"]:
            assert isinstance(episode["disneyplus_id"], str)

        # Simpsonsworld ID should be an int if set
        if episode["simpsonsworld_id"]:
            assert isinstance(episode["simpsonsworld_id"], int)

        # Good should be a boolean
        assert isinstance(episode["good"], bool)

        # Guest stars, directors, writers should be an array of strings
        if episode["guest_stars"]:
            assert isinstance(episode["guest_stars"], list)
            for star in episode["guest_stars"]:
                assert isinstance(star, str)

        if episode["writers"]:
            assert isinstance(episode["writers"], list)
            for writer in episode["writers"]:
                assert isinstance(writer, str)

        if episode["directors"]:
            assert isinstance(episode["directors"], list)
            for director in episode["directors"]:
                assert isinstance(director, str)

    # Season-Episode pair should be unique
    assert len(all_episodes) == len(
        set(f"{ep['season']}-{ep['episode']}" for ep in all_episodes)
    )

print("QA complete!")
