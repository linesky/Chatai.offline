import tkinter as tk
import pygame.midi
#pip install pygame
# Inicializar o pygame.midi
pygame.midi.init()

# Selecionar o dispositivo de saída MIDI
output_id = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(output_id)
notas_midi=[]
# Definir as notas MIDI para um piano de acordo médio
for notes in range(20,100,2):
    notas_midi =  notas_midi + [notes]

def tocar_nota(nota):
    """Função para tocar uma nota MIDI."""
    midi_out.note_on(nota, 127)  # Tocar a nota com a velocidade máxima (127)
    root.after(500, lambda: midi_out.note_off(nota, 127))  # Parar a nota após 500 ms

# Configurar a janela principal
root = tk.Tk()
root.title("Piano MIDI")
root.geometry("600x480")
root.configure(bg="white")

# Criar botões para cada nota
iii=0
ii=0
i1=0
for i, nota in enumerate(notas_midi):
    btn = tk.Button(root, text=f"Nota {nota}", command=lambda nota=nota: tocar_nota(nota))
    btn.grid(row=ii, column=iii, padx=5, pady=5)
    iii=iii+1
    if iii> 7:
        iii=0
        ii=ii+1
# Executar a aplicação
root.mainloop()

# Fechar o dispositivo de saída MIDI ao finalizar a aplicação
midi_out.close()
pygame.midi.quit()

