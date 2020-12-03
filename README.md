<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/itunes.svg?maxAge=3600)](https://pypi.org/project/itunes/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/itunes.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/itunes.py/actions)

### Installation
```bash
$ [sudo] pip install itunes
```

#### Examples
`vlc.tell(applescript)` - execute applescript `tell application "VLC" ...`
```python
>>> itunes.tell('play')
```

```python
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

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
