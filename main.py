import flet as ft
import json as js
import pygame

pygame.mixer.init()

# Variáveis globais
color_music = None
musica = None
music_list = [0]
play = False
musica_path = None
resume = False

def main(page: ft.Page):
    
    # Banco de dados das músicas
    with open("database.json", "r") as f:
        data = js.load(f)
    
    global music_list
    music_list = data["musicas"]
    
    musica = music_list[0]  # A primeira música

    #Play e pause
    def play_stop(e):
        global resume
        global play
        global musica_path
        if play == False:
            play = True
            play_btn.icon=ft.icons.PAUSE_CIRCLE_FILLED_OUTLINED
            if musica == music_list[0]:
                if  resume == True:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.load(musica_path)
                    pygame.mixer.music.play()
            elif musica == music_list[1]:
                if  resume == True:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.load(musica_path)
                    pygame.mixer.music.play()

            elif musica == music_list[2]:
                if  resume == True:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.load(musica_path)
                    pygame.mixer.music.play()

            elif musica == music_list[3]:
                if  resume == True:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.load(musica_path)
                    pygame.mixer.music.play()
                
        else:
            play = False
            play_btn.icon=ft.icons.PLAY_CIRCLE_FILLED_OUTLINED
            if musica == music_list[0]:
                pygame.mixer.music.pause()
                resume = True
                
            elif musica == music_list[1]:
                pygame.mixer.music.pause()
                resume = True
                
            elif musica == music_list[2]:
                pygame.mixer.music.pause()
                resume = True
    
                
            elif musica == music_list[3]:
                pygame.mixer.music.pause()
                resume = True
                
        page.update()
    
    # Função que altera a música
    def next(e):
        global play
        global resume
        global musica_path
        global musica
        # Alternar para a próxima música
        if musica == music_list[0]:
            musica = music_list[1]
        elif musica == music_list[1]:
            musica = music_list[2]
        elif musica == music_list[2]:
            musica = music_list[3]
        else:
            musica = music_list[0]
        
        # Atualiza os controles na interface
        name_msc.value = musica["nome"]
        msc_img.src = musica["imagem"]
        musica_path = musica["som"]
        
        global color_music
        if musica == music_list[0]:
            color_music = ft.colors.AMBER
        elif musica == music_list[1]:
            color_music = ft.colors.RED
        elif musica == music_list[2]:
            color_music = ft.colors.BLUE_ACCENT
        elif musica == music_list[3]:
            color_music = ft.colors.RED_ACCENT
        

        play_btn.icon_color = color_music
        line_msc.active_color = color_music
        next_btn.icon_color = color_music
        prev_btn.icon_color = color_music
        image.border= border=ft.border.all(5, color_music)
        name_msc.color = color_music
        name_msc.style.decoration_color = color_music
        
        resume = False
        play = False
        pygame.mixer.music.stop()
        play_btn.icon=ft.icons.PLAY_CIRCLE_FILLED_OUTLINED
        
        page.update()  # Atualiza a interface após mudanças
    
    #Voltar a musica
    def prev(e):
        global play
        global resume
        global musica
        # Alternar para a próxima música
        if musica == music_list[0]:
            musica = music_list[3]
        elif musica == music_list[3]:
            musica = music_list[2]
        elif musica == music_list[2]:
            musica = music_list[1]
        else:
            musica = music_list[0]
        
        # Atualiza os controles na interface
        name_msc.value = musica["nome"]
        msc_img.src = musica["imagem"]
        
        global color_music
        if musica == music_list[0]:
            color_music = ft.colors.AMBER
        elif musica == music_list[1]:
            color_music = ft.colors.RED
        elif musica == music_list[2]:
            color_music = ft.colors.BLUE_ACCENT
        elif musica == music_list[3]:
            color_music = ft.colors.RED_ACCENT
        

        play_btn.icon_color = color_music
        line_msc.active_color = color_music
        next_btn.icon_color = color_music
        prev_btn.icon_color = color_music
        image.border= border=ft.border.all(5, color_music)
        name_msc.color = color_music
        name_msc.style.decoration_color = color_music
        
        resume = False
        play = False
        pygame.mixer.music.stop()
        play_btn.icon=ft.icons.PLAY_CIRCLE_FILLED_OUTLINED
        
        page.update()  # Atualiza a interface após mudanças

    # Configuração inicial da página
    page.title = "Music Player"
    page.window_height = 800
    page.window_width = 500
    page.window_maximizable = False
    page.window_resizable = False
    page.bgcolor = ft.colors.BLUE_GREY_900
    
    # Componentes da interface
    name_msc = ft.Text(value=musica["nome"], size=50,color=color_music,
                       style=ft.TextStyle(
                        decoration=ft.TextDecoration.UNDERLINE,
                        decoration_color=color_music
                       ))
    
    play_btn = ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILLED_OUTLINED,
                             icon_color=color_music,
                             icon_size=40,
                             on_click=play_stop)
    
    next_btn = ft.IconButton(icon=ft.icons.SKIP_NEXT_OUTLINED,
                             icon_color=color_music,
                             icon_size=25,
                             on_click=next)
    
    prev_btn = ft.IconButton(icon=ft.icons.SKIP_PREVIOUS_OUTLINED,
                             icon_color=color_music,
                             icon_size=25,
                             on_click=prev)
    
    line_msc = ft.Slider(min=0, max=100,
                         inactive_color=ft.colors.BLACK12,
                         active_color=color_music,
                         expand=True)
    
    msc_img = ft.Image(src=musica["imagem"])
    
    image = ft.Container(content=msc_img,
                         margin=30,
                         border=ft.border.all(5, color_music),
                         border_radius=15)
    
    title_row = ft.Row(controls=[name_msc],
                       alignment=ft.MainAxisAlignment.CENTER)
    
    player_row = ft.Row(controls=[prev_btn, play_btn, next_btn, line_msc],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=0)
    
    layout = ft.Column(controls=[title_row, image, player_row],
                       alignment=ft.MainAxisAlignment.CENTER,
                       expand=True)
    
    page.add(layout)
    page.update()  # Atualiza a interface na inicialização

ft.app(target=main, assets_dir="img")
