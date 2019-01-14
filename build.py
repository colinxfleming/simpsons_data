"""A series of asserts to verify data quality."""
import json

with open('simpsons_data.json', 'r') as f:
    all_json = json.load(f)
    all_episodes = all_json['episodes']
    all_characters = all_json['characters']

    # EPISODE QA #

    for episode in all_episodes:
        # Title should be a string
        assert isinstance(episode['title'], str)
        assert len(episode['title']) > 0

        # Season should be an int
        assert isinstance(episode['season'], int)

        # Episode should be an int
        assert isinstance(episode['episode'], int)

        # Description should be a string
        assert isinstance(episode['description'], str)

        # Simpsonsworld ID should be an int
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

        # Characters should exist in the corresponding Characters blob

    # CHARACTER QA #

    # Character name should be unique

    # Character shortname should be unique
