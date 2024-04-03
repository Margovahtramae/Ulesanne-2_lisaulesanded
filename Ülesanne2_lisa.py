# Impordib pygame'i mooduli
import pygame
import sys
import math

# Initsialiseerib pygame'i
pygame.init()

# Määra mängu ekraani suurus
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ülessane2")

# Määra pildi täielik tee
bg_path = "Lisa_pildid/bg_shop.jpg"
# Lae taustapilt
bg = pygame.image.load(bg_path)

# Laeb müüja pildi ja määrab selle suuruseks 250x300 pikslit
sell_path = "Lisa_pildid/seller.png"
sell = pygame.image.load(sell_path)
sell = pygame.transform.scale(sell, [250, 300])

# Laeb jutumulli pildi ja muudab selle suurust 80% võrra
chat_path = "Lisa_pildid/chat.png"
chat = pygame.image.load(chat_path)
scale_factor = 0.80
chat = pygame.transform.scale(chat, [int(chat.get_width() * scale_factor), int(chat.get_height() * scale_factor)])

# Initsialiseerib pygame'i fondi
pygame.font.init()

# Loob fondi suurusega 21 punkti
font = pygame.font.Font(pygame.font.match_font("none"), 21)

# Loob teksti pildi, kasutades eelnevalt loodud fonti, valget värvi ja teksti "Tere, Margo-Marten Vahtramäe"
text = font.render("Tere, Margo-Marten Vahtramäe", True, [255,255,255])

# Määrab teksti laiuse ja kõrguse
text_width = text.get_rect().width
text_height = text.get_rect().height

# Lisa VIKK100 logo
logo_path = "Lisa_pildid/vikk100_logo.png"
logo = pygame.image.load(logo_path)
logo = pygame.transform.scale(logo, [300, 50])

# Lisa mõõk seina peale
sword_path = "Lisa_pildid/mõõk.png"
sword = pygame.image.load(sword_path)
sword = pygame.transform.scale(sword, [100, 100])

# Lisa tort
cake_path = "Lisa_pildid/cake.png"
cake = pygame.image.load(cake_path)
cake = pygame.transform.scale(cake, [80, 80])

# Lisa kaarega tekst "TULEVIK 2050"
def draw_text_arc(screen, font, color, radius, angle, text):
    for i, char in enumerate(text):
        char_render = font.render(char, True, color)
        char_width = char_render.get_width()
        char_height = char_render.get_height()
        char_angle = angle - (i / len(text)) * math.pi
        x = screen_width // 2 + int(radius * math.cos(char_angle)) - char_width // 2   # Lisasin 50 pikslit nihet paremale
        y = screen_height // 12 - int(radius * math.sin(char_angle)) - char_height // 2
        screen.blit(char_render, (x, y))

# Määra kaare parameetrid
arc_radius = 50
arc_angle = math.pi / 6  # 45 kraadi

# Seab muutuja "running" väärtuseks "True"
running = True

# Mängutsükkel
while running:
    # Käsitseb sündmusi
    for event in pygame.event.get():
        # Kui kasutaja vajutab sulgemisnuppu
        if event.type == pygame.QUIT:
            # Muudab muutuja "running" väärtuseks "False", mis peatab mängutsükli
            running = False

    # Asetab taustapildi mängu aknale
    screen.blit(bg,[0,0])
    # Asetab müüja pildi mängu aknale koordinaatidele (105,160)
    screen.blit(sell,[105,160])
    # Asetab jutumulli pildi mängu aknale koordinaatidele (245,85)
    screen.blit(chat,[245,85])

    # Arvutab teksti x- ja y-koordinaadid nii, et tekst oleks keskel
    text_x = (screen.get_width() - text_width) // 2
    text_y = (screen.get_height() - text_height) // 2
    # Asetab teksti mängu aknale koordinaatidele (365-text_width/2, 160-text_height/2)
    screen.blit(text, [365-text_width/2,160-text_height/2])
    
    # Asetab logo vasakusse nurka
    screen.blit(logo, [20, 5])
    
    # Asetab mõõk seina peale
    screen.blit(sword, [538, 150])

    # Asetab tort lauale
    screen.blit(cake, [428, 220])
    
    # Asetab kaarega tekst "TULEVIK 2050"
    draw_text_arc(screen, font, (255, 255, 255), arc_radius, arc_angle, "TULEVIK 2050")
    
    # Värskendab mänguakent
    pygame.display.flip()

# Lõpetab pygame'i kasutamise
pygame.quit()


