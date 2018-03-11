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
characters: Unimplemented at present. Focus character(s), if any.
```

`Characters` are shaped as follows:

```yml
short_name: String. Common name or nickname, unique reference key.
name: String. Full name.
core_family: Boolean. True if they are Homer, Marge, Lisa, Bart, or Maggie.
```
### Episode coverage

There's a lot of episodes and seasons to go through and mark the good ones.
Here's what's done so far:

* **Season 1**: Not done
* **Season 2**: Not done
* **Season 3**: Not done
* **Season 4**: Not done
* **Season 5**: Not done
* **Season 6**: Mostly done
* **Season 7**: Not done
* **Season 8**: Not done
* **Season 9**: Not done
* **Season 10**: Not done
* **Season 11**: Not done
* **Season 12**: Not done
* **Season 13**: Not done
* **Season 14**: Not done
* **Season 15**: Not done
* **Season 16**: Not done
* **Season 17**: Not done
* **Season 18**: Not done
* **Season 19**: Not done
* **Season 20**: Not done
* **Season 21**: Not done
* **Season 22**: Not done
* **Season 23**: Not done
* **Season 24**: Not done
* **Season 25**: Not done
* **Season 26**: Not done
* **Season 27**: Not done
* **Season 28**: Not done
* **Season 29**: Not done

## Usage

`python compile_data.py` spits out a json file with keys characters and episodes.

<strike>`./compile_seasons.py yaml` spits out a yaml file.</strike> (Coming soon)

There are current versions of these in the base directory for your convenience.

## Suggestions welcome

Please put in issues if you have anything you'd like to add.
