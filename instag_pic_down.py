
'''Lets say you need a few images on a particular hashtag 
from Instagram. Its as easy as 3 lines of code !'''

import instaloader

loader = instaloader.Instaloader(download_videos=False, save_metadata=False, post_metadata_txt_pattern='')
loader.download_hashtag('DevOps', max_count=10)

'''This code will create a new folder with name #DevOps
and will have 10 latest images with #DevOps.'''
# !! pip3 install instaloader