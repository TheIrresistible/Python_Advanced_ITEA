import requests
from threading import Thread


urls = ['https://gate.undelete.news/uploads//bmthofficial/BALXwWz-_400x400.jpg',
        'https://yt3.ggpht.com/a/AATXAJz0cwg9bcQ80BxpWs1JqK3w06o0QPoQ2XuP6MW1YA=s900-c-k-c0xffffffff-no-rj-mo',
        'https://upload.wikimedia.org/wikipedia/commons/a/ab/Cover-art-mother-tongue.jpg',
        'https://c4.wallpaperflare.com/wallpaper/366/526/566/bring-me-the-horizon-logo-wallpaper-preview.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRY5xcr2lacDIYHrlzO3h-fZzkBGiGlYl_Uxg&usqp=CAU',
        'https://i.pinimg.com/originals/68/65/34/6865345065f9615d4cef0ea9bd85f408.jpg',
        'https://img.youtube.com/vi/A2vHIpxsfEM/0.jpg',
        'https://1.bp.blogspot.com/-WxMn2S0XR2I/UQ5d8UByxfI/AAAAAAAAAXE/2XZmVfzwwSA/s640/Wolf.jpg',
        'https://www.punkvideosrock.com/wp-content/uploads/2015/01/Falling-In-Reverse-2014.jpg',
        'https://s3.amazonaws.com/s3.timetoast.com/public/uploads/photos/3425210/falling_in_reverse.jpg']


def threaded(fn):

    def wrapper(daemon, name, *args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs, name=name, daemon=daemon)
        thread.start()
        return thread
    return wrapper


@threaded
def downloader(url, name):
    print(f'{url} started downloading')
    r = requests.get(url, allow_redirects=True)
    open(f'{name}.jpg', 'wb').write(r.content)
    print(f'{url} finished downloading')


downloader(False, '1', urls[0], '1 image')
downloader(False, '2', urls[1], '2 image')
downloader(False, '3', urls[2], '3 image')
downloader(False, '4', urls[3], '4 image')
downloader(False, '5', urls[4], '5 image')
downloader(False, '6', urls[5], '6 image')
downloader(False, '7', urls[6], '7 image')
downloader(False, '8', urls[7], '8 image')
downloader(False, '9', urls[8], '9 image')
downloader(False, '10', urls[9], '10 image')
