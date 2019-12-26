#!/usr/bin/env python

"""A series of asserts to verify data quality."""
import json

expected_ep_keys = ['title', 'season', 'episode', 'description', 'disneyplus_id',
                    'simpsonsworld_id', 'good', 'characters']
expected_char_keys = ['name', 'short_name']

print('loading file...')

with open('simpsons_data.json', 'r') as f:
    all_json = json.load(f)
    all_episodes = all_json['episodes']
    all_characters = all_json['characters']

    # EPISODE QA #

    print('QAing episodes...')

    for episode in all_episodes:
        # Should have expected keys
        # print(f"#{episode['season']} - #{episode['episode']}")
        for key in expected_ep_keys:
            assert key in episode
        assert len(expected_ep_keys) == len(episode.keys())

        # Title should be a string
        assert isinstance(episode['title'], str)
        assert len(episode['title']) > 0

        # Season should be an int
        assert isinstance(episode['season'], int)
        # assert episode['season'] < 50

        # Episode should be an int
        assert isinstance(episode['episode'], int)
        # assert episode['episode'] < 50

        # Description should be a string
        assert isinstance(episode['description'], str)

        # Simpsonsworld ID should be a str if set
        if episode['disneyplus_id']:
            assert isinstance(episode['disneyplus_id'], str)

        # Simpsonsworld ID should be an int if set
        if episode['simpsonsworld_id']:
            assert isinstance(episode['simpsonsworld_id'], int)

        # Good should be a boolean
        assert isinstance(episode['good'], bool)

        # Characters should be an array of strings
        assert isinstance(episode['characters'], list)
        for character in episode['characters']:
            assert isinstance(character, str)

            # Every character should exist in the corresponding characters blob
            assert next(char for char in all_characters
                        if char['short_name'] == character)

    # Season-Episode pair should be unique
    assert len(all_episodes) == len(set(f"{ep['season']}-{ep['episode']}"
                                        for ep in all_episodes))

    # CHARACTER QA #

    print('QAing characters...')

    for character in all_characters:
        # Should have expected keys
        for key in expected_char_keys:
            assert key in character
        assert len(expected_char_keys) == len(character.keys())

        # Name should be a string
        assert isinstance(character['name'], str)

        # Short name should be a string
        assert isinstance(character['short_name'], str)

    # Character name should be unique
    assert len(all_characters) == len(set(f"#{char['name']}"
                                          for char in all_characters))

    # Character shortname should be unique
    assert len(all_characters) == len(set(f"#{char['short_name']}"
                                          for char in all_characters))

print('QA complete!')
