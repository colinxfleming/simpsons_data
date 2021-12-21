# A dataset of Simpsons episodes

Please enjoy this dataset of Simpsons data, scraped from SimponsWorld.

## Contents

This contains episodes and characters split out into yaml files, which gets boiled down to a json file, which gets loaded into [Simpsons Optimizer](https://www.simpsonsoptimizer.com/).

## Contributing

* Change episode or character in the yaml files
* Open pull request

## Data model

`Episodes` are shaped as follows:

```yml
title: String. Episode title.
season: Integer. Season number.
episode: Integer. Episode number.
description: String. Episode description from SimpsonsWorld.
disneyplus_id: String. Episode video identifier on DisneyPlus.
simpsonsworld_id: BigInt. Episode video identifier from SimpsonsWorld (legacy).
good: Boolean. Indicator of whether or not the episode is bad.
guest_stars: Array of strings. Strings are guest star's name. 
```

### Episode coverage

There's a lot of episodes and seasons to go through and mark the good ones.
Episodes' goodness defaults to false. You can see what's still pending by running `./remaining_report.py`.

## Usage

`python compile_data.py` spits out a json file with episodes.

There are current versions of these in the base directory for your convenience.

## Suggestions welcome

Please put in issues if you have anything you'd like to add.
