import instaloader

insta = instaloader.Instaloader()
profile = input('Enter Your Profile Name : ')
insta.download_profile(profile,profile_pic_only=True)