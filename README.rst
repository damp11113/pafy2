Features
--------

- Retreive metadata such as viewcount, duration, rating, author, thumbnail, keywords
- Download video or audio at requested resolution / bitrate / format / filesize
- Command line tool (ytdl) for downloading directly from the command line
- Retrieve the URL to stream the video in a player such as vlc or mplayer
- Works with age-restricted videos and non-embeddable videos
- Small, standalone, single importable module file (pafy2.py)
- Select highest quality stream for download or streaming
- Download video only (no audio) in m4v or webm format
- Download audio only (no video) in ogg or m4a format
- Retreive playlists and playlist metadata
- Works with Python 3.6+
- Optionally depends on yt_dlp (recommended; more stable)
- Fast fetch and download

Installation
------------

pafy2 can be installed using `pip <http://www.pip-installer.org>`_:

.. code-block:: bash

    $ [sudo] pip install git+https://github.com/damp11113/pafy2.git

or use a `virtualenv <http://virtualenv.org>`_ if you don't want to install it system-wide:

.. code-block:: bash

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install git+https://github.com/damp11113/pafy2.git

Documentation
-------------

Full documentation is available at http://pythonhosted.org/pafy (is not pafy2)

Usage Examples
--------------

Here is how to use the module in your own python code.  For command line tool
(ytdl) instructions, see further below

.. code-block:: pycon

    >>> import pafy2

create a video instance from a YouTube url:

.. code-block:: pycon

    >>> url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
    >>> video = pafy2.new(url)

get certain attributes:

.. code-block:: pycon
    
    >>> video.title
    'Richard Jones: Introduction to game programming - PyCon 2014'

    >>> video.rating
    5.0

    >>> video.viewcount, video.author, video.length
    (1916, 'PyCon 2014', 10394)

    >>> video.duration, video.likes, video.dislikes
    ('02:53:14', 25, 0)

    >>> print(video.description)
    Speaker: Richard Jones

    This tutorial will walk the attendees through development of a simple game using PyGame with time left over for some experimentation and exploration of different types of games.

    Slides can be found at: https://speakerdeck.com/pycon2014 and https://github.com/PyCon/2014-slides


list available streams for a video:

.. code-block:: pycon

    >>> streams = video.streams
    >>> for s in streams:
    ...     print(s)
    ...
    normal:mp4@1280x720
    normal:webm@640x360
    normal:mp4@640x360
    normal:flv@320x240
    normal:3gp@320x240
    normal:3gp@176x144


show all formats, file-sizes and their download url:

.. code-block:: pycon

    >>> for s in streams:
    ...    print(s.resolution, s.extension, s.get_filesize(), s.url)
    ...
    1280x720 mp4 2421958510 https://r1---sn-aiglln7e.googlevideo.com/videoplayba[...]
    640x360 webm 547015732 https://r1---sn-aiglln7e.googlevideo.com/videoplaybac[...]
    640x360 mp4 470655850 https://r1---sn-aiglln7e.googlevideo.com/videoplayback[...]
    320x240 flv 345455674 https://r1---sn-aiglln7e.googlevideo.com/videoplayback[...]
    320x240 3gp 208603447 https://r1---sn-aiglln7e.googlevideo.com/videoplayback[...]
    176x144 3gp 60905732 https://r1---sn-aiglln7e.googlevideo.com/videoplayback?[...]


get best resolution regardless of file format:

.. code-block:: pycon

    >>> best = video.getbest()
    >>> best.resolution, best.extension
    ('1280x720', 'mp4')


get best resolution for a particular file format:
(mp4, webm, flv or 3gp)

.. code-block:: pycon

    >>> best = video.getbest(preftype="webm")
    >>> best.resolution, best.extension
    ('640x360', 'webm')

get url, for download or streaming in mplayer / vlc etc:

.. code-block:: pycon
    
    >>> best.url
    'http://r12---sn-aig7kner.c.youtube.com/videoplayback?expire=1369...

Download video and show progress:

.. code-block:: pycon

    >>> best.download(quiet=False)
    3,734,976 Bytes [0.20%] received. Rate: [ 719 KB/s].  ETA: [3284 secs]

Download video, use specific directory and/or filename:

.. code-block:: pycon

    >>> filename = best.download(filepath="/tmp/")

    >>> filename = best.download(filepath="/tmp/Game." + best.extension)

Get audio-only streams (m4a and/or ogg vorbis):

.. code-block:: pycon

    >>> audiostreams = video.audiostreams
    >>> for a in audiostreams:
    ...     print(a.bitrate, a.extension, a.get_filesize())
    ...
    256k m4a 331379079
    192k ogg 172524223
    128k m4a 166863001
    128k ogg 108981120
    48k m4a 62700449


Download the 2nd audio stream from the above list:

.. code-block:: pycon

    >>> audiostreams[1].download()

Get the best quality audio stream:

.. code-block:: pycon

    >>> bestaudio = video.getbestaudio()
    >>> bestaudio.bitrate
    '256'

Download the best quality audio file:

.. code-block:: pycon

    >>> bestaudio.download()

show all media types for a video (video+audio, video-only and audio-only):

.. code-block:: pycon

    >>> allstreams = video.allstreams
    >>> for s in allstreams:
    ...     print(s.mediatype, s.extension, s.quality)
    ...

    normal mp4 1280x720
    normal webm 640x360
    normal mp4 640x360
    normal flv 320x240
    normal 3gp 320x240
    normal 3gp 176x144
    video m4v 1280x720
    video webm 1280x720
    video m4v 854x480
    video webm 854x480
    video m4v 640x360
    video webm 640x360
    video m4v 426x240
    video webm 426x240
    video m4v 256x144
    video webm 256x144
    audio m4a 256k
    audio ogg 192k
    audio m4a 128k
    audio ogg 128k
    audio m4a 48k
