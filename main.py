from moviepy import VideoFileClip, vfx

# from moviepy.video.fx import vfx

# 원본 mov 파일 불러오기
clip = VideoFileClip("input.mov") # input 파일명(위치 상관 o)

# 10배속으로 만들기
clip_10x = clip.with_effects([vfx.MultiplySpeed(10), vfx.Resize(height=480)])

# 필요시 해상도 줄이기 (선택)
# clip_10x = clip_10x

# gif로 저장
clip_10x.write_gif("output.gif", fps=15) # output 파일명 o