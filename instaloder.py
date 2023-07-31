
import instaloader
ig=instaloader.Instaloader()
dp=input("enter the insta username:")
ig.download_profile(dp,profile_pic_only=False)