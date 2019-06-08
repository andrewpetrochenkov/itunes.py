<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/itunes.svg?longCache=True)](https://pypi.org/project/itunes/)
[![](https://img.shields.io/pypi/v/itunes.svg?maxAge=3600)](https://pypi.org/project/itunes/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/itunes.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/itunes.py/)

#### Installation
```bash
$ [sudo] pip install itunes
```

#### Functions
function|`__doc__`
-|-
`itunes.activate()` |open iTunes and make it frontmost
`itunes.frontmost()` |return True if `iTunes.app` is frontmost app, else False
`itunes.kill()` |
`itunes.mute()` |mute iTunes
`itunes.muted()` |return True if iTunes muted, else False
`itunes.next()` |play next track
`itunes.pid()` |return iTunes.app pid
`itunes.prev()` |play previous track
`itunes.quit()` |Quit iTunes
`itunes.state()` |return player state string
`itunes.stop()` |stop
`itunes.tell(code)` |execute applescript `tell application "iTunes" ...`
`itunes.unmute()` |unmute iTunes
`itunes.helper.tell(code)` |
`itunes.playlists.names()` |
`itunes.playlists.play(playlist_name)` |
`itunes.tracks.play(track, playlist)` |
`itunes.volume.change(value)` |
`itunes.volume.get()` |

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
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>