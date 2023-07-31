from pytube import YouTube

#link = "https://www.youtube.com/watch?v=1sP8ZpeM0Ak&list=RDCLAK5uy_ksEjgm3H_7zOJ_RHzRjN1wY-_FFcs7aAU"
link="https://www.youtube.com/watch?v=X458ZhwKKbk&list=RDX458ZhwKKbk&start_radio=1"
#link="enter the you tube video link:"
YouTube_1 = YouTube(link)

#print(YouTube_1.title)
#print(YouTube_1.thumbnail_url) 

#vidio = YouTube_1.streams.all()
video=YouTube_1.streams.filter(only_audio=True)
vid = list(enumerate(video))
for i in vid:
    print(i)
print()
strm=int(input("enter the number for install video quality :"))    

# video[strm].download()
# print("successfully")
# import instaloader
# ig=instaloader.Instaloader()
# dp=input("enter the insta username:")
# ig.download_profile(dp,profile_pic_only=False)