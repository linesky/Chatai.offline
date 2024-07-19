import time
import pygame.midi
#pip install pygame
# Inicializar o pygame.midi
pygame.midi.init()
print("\x1bc\x1b[47;34m")
def tocar_nota(nota):
    """Função para tocar uma nota MIDI."""
    midi_out.note_on(nota, 127)  # Tocar a nota com a velocidade máxima (127)
    time.sleep(0.5)  # Parar a nota após 500 ms

# Selecionar o dispositivo de saída MIDI
output_id = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(output_id)
notas_midi=[]
# Definir as notas MIDI para um piano de acordo médio




a=input("file name?")
f1=open(a,"r")
aa=f1.read()
f1.close()

iii=0
ii=0
i1=0
bb=aa.split("\n")

for bb1 in bb:
    cc=bb1.split(",")
    for cc1 in cc:
        cc1=cc1.strip()
        if cc1!="":
            tocar_nota(int(cc1))
    
# Executar a aplicação
# Fechar o dispositivo de saída MIDI ao finalizar a aplicação
midi_out.close()
pygame.midi.quit()

