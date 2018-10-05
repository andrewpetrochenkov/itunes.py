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
>>> itunes.playlists.names()
["playlist1","playlist2"]

>>> itunes.playlists.play("playlist1")
```

play_track
```python
>>> itunes.tracks.play("track_name","playlist")
```

volume
```python
>>> itunes.volume.change(10)
>>> itunes.volume.get()
10
```

mute
```python
>>> itunes.mute()
>>> itunes.muted()
True
>>> itunes.unmute()
```


process
```python
>>> itunes.pid()
7654
>>> itunes.kill()
```