from pytube import YouTube
import moviepy.editor as mp
import re
import os

def baixa(link, path):
    print("Bem vindo ao Pytube!")
    link = input("Digite o link do vídeo do YouTube que deseja baixar: ")
    path = "G:\\Meu Drive\\Músicas baixadas py"
    print(path)
    yt = YouTube(link)

    print("Baixando...")
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print("Download concluído!")

    print("Convertendo arquivo...")
    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
    print("Sucesso!")

baixa(1,1)