"""practico_gif

Usage:
  practico_gif.py <archivo> --inicio=<inicio> --fin=<fin> [--redimensionar=<redimensionar>]

Options:
  -h --help     Show this screen. 

"""
from docopt import docopt
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

def clip_gif(archivo, inicio, fin, redimensionar=None):
    v = VideoFileClip(archivo) # cargamos el archivo de video como un objeto a moviepy
    v2 = v.subclip(inicio, fin)     # recortamos la porcion que nos interesa
    v3 = v2.fx(vfx.time_mirror)     # hacemos una version "reversa" de v2
    vfinal= concatenate_videoclips([v2, v3]) # concatena v1 y v2  # SE CAMBIO:aqui va punto para una nueva funcion .resize()
    if redimensionar:
        vfinal=vfinal.resize(redimensionar)
    gif = archivo[0:-4] + '.gif'   # Guarda el archivo resultante como gif
    #print('Se guardo '+gif)
    vfinal.write_gif(gif, fps=15) #aqui si va coma luego del gif

if __name__ == '__main__':
    argumentos = docopt(__doc__) 
    #print(argumentos)
    archivo = argumentos['<archivo>']
    inicio = float(argumentos['--inicio'])
    fin = float(argumentos['--fin'])
    redimensionar = (argumentos['--redimensionar'])
    if redimensionar:
        redimensionar=float(redimensionar)
    clip_gif(archivo, inicio, fin, redimensionar)

