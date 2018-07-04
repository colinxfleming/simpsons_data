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
characters: Array of strings. Strings are character short_names. 
```

`Characters` are shaped as follows:

```yml
short_name: String. Lowercase common name or nickname, unique reference key.
name: String. Full name.
```
### Episode coverage

There's a lot of episodes and seasons to go through and mark the good ones.
Here's what's done so far:

* **Season 1**: Episodes cataloged; Characters uncataloged
* **Season 2**: Episodes cataloged; Characters uncataloged
* **Season 3**: Episodes cataloged; Characters uncataloged
* **Season 4**: Episodes cataloged; Characters uncataloged
* **Season 5**: Episodes cataloged; Characters uncataloged
* **Season 6**: Episodes cataloged; Characters uncataloged
* **Season 7**: Episodes cataloged; Characters uncataloged
* **Season 8**: Episodes cataloged; Characters uncataloged
* **Season 9**: Episodes cataloged; Characters uncataloged
* **Season 10**: Episodes cataloged; Characters uncataloged
* **Season 11**: Episodes uncataloged; Characters uncataloged
* **Season 12**: Episodes uncataloged; Characters uncataloged
* **Season 13**: Episodes uncataloged; Characters uncataloged
* **Season 14**: Episodes uncataloged; Characters uncataloged
* **Season 15**: Episodes uncataloged; Characters uncataloged
* **Season 16**: Episodes uncataloged; Characters uncataloged
* **Season 17**: Episodes uncataloged; Characters uncataloged
* **Season 18**: Episodes uncataloged; Characters uncataloged
* **Season 19**: Episodes uncataloged; Characters uncataloged
* **Season 20**: Episodes uncataloged; Characters uncataloged
* **Season 21**: Episodes uncataloged; Characters uncataloged
* **Season 22**: Episodes uncataloged; Characters uncataloged
* **Season 23**: Episodes uncataloged; Characters uncataloged
* **Season 24**: Episodes uncataloged; Characters uncataloged
* **Season 25**: Episodes uncataloged; Characters uncataloged
* **Season 26**: Episodes uncataloged; Characters uncataloged
* **Season 27**: Episodes uncataloged; Characters uncataloged
* **Season 28**: Episodes uncataloged; Characters uncataloged
* **Season 29**: Episodes uncataloged; Characters uncataloged

## Usage

`python compile_data.py` spits out a json file with keys characters and episodes.

<strike>`./compile_seasons.py yaml` spits out a yaml file.</strike> (Coming soon)

There are current versions of these in the base directory for your convenience.

## Suggestions welcome

Please put in issues if you have anything you'd like to add.
