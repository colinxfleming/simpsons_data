# A dataset of Simpsons episodes

Please enjoy this dataset of Simpsons data, scraped from SimponsWorld.

## Contents

Season data is in its own individual file, which gets compiled by a python script.

## Data model

`Episodes` are shaped as follows:

```yml
title: String. Episode title.
season: Integer. Season number.
episode: Integer. Episode number.
description: String. Episode description from SimpsonsWorld.
simpsonsworld_id: BigInt. Episode video identifier from SimpsonsWorld.
good: Boolean. Indicator of whether or not the episode is bad.
character: Unimplemented at present. Focus character, if any.
```

`Characters` are TK.

## Usage

`./compile_seasons.py json` spits out a json file with keys characters and episodes.

`./compile_seasons.py yaml` spits out a yaml file.

## Suggestions welcome

Please put in issues if you have anything you'd like to add.
