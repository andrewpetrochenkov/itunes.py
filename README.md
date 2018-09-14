[![](https://img.shields.io/pypi/pyversions/itunes.svg?longCache=True)](https://pypi.org/pypi/itunes/)
[![](https://img.shields.io/pypi/v/itunes.svg?maxAge=3600)](https://pypi.org/pypi/itunes/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/itunes.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/itunes.py/)

### Install
```bash
$ [sudo] pip install itunes
```

### Examples
```python
import itunes
>>> itunes.play()
>>> itunes.pause()
>>> itunes.stop()
>>> itunes.next()
>>> itunes.prev()
```

playlists
```python
>>> itunes.playlists()
["playlist1","playlist2"]
```

play_track
```python
>>> itunes.play_track("track_name","playlist")
>>> itunes.play_track(1,"playlist")
```

volume
```python
>>> itunes.volume(10)
>>> itunes.volume()
10
```
mute
```python
>>> itunes.mute()
>>> itunes.muted()
True
>>> itunes.unmute()
```