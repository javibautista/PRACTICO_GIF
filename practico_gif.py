#PRACTICO GIF

from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
v = VideoFileClip(‘cat.mp4’) #introducimos el video a una variable
v2= v.subclip(1, 2) #tomamos los segundos del 1 al 2
v3= v2.fx(vfx.time_mirror) # llamamos a la funcion espejo de tiempo
vfinal= concatenate_videoclips([v2, v3]).resize(0.25) #aqui va punto para una nueva funcion
vfinal.write_gif(‘catBoomerang.gif’, fps=15) #aqui si va coma luego del gif

# !eog catBoomerang.gif # reproduzco el practico final #
