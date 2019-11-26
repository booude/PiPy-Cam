#Importar módulo OS que roda o script no Terminal
import os
import PySimpleGUI as sg

#Variável para diferenciar fotos
n=1

#Interface em PySimpleGUI para configurar a câmera
sg.change_look_and_feel('LightBlue')

layout = [
  [sg.Text('Opacidade'),sg.Slider(range=(0,255), default_value=255, size=(20,10), orientation='horizontal',font=('Helvetica', 12)), sg.Text('Nitidez'),sg.Slider(range=(-100,100), default_value=0, size=(20,10), orientation='horizontal', font=('Helvetica', 12))],

  [sg.Text('Contraste'),sg.Slider(range=(-100,100), default_value=0, size=(20,10), orientation='horizontal',font=('Helvetica', 12)), sg.Text('Brilho'),sg.Slider(range=(0,100), default_value=50, size=(20,10), orientation='horizontal', font=('Helvetica', 12))],

  [sg.Text('Saturação'),sg.Slider(range=(-100,100), default_value=0, size=(20,10), orientation='horizontal',font=('Helvetica', 12)), sg.Text('ISO'),sg.Slider(range=(100,800), default_value=800, size=(20,10), orientation='horizontal', font=('Helvetica', 12))],

  [sg.Text('Exposição'),sg.Slider(range=(-10,10), default_value=0, size=(20,10), orientation='horizontal',font=('Helvetica', 12))],
  
  [sg.Text('Abertura'),sg.Slider(range=(0,600000), default_value=8000, size=(45,10), orientation='horizontal', font=('Helvetica', 12))],

  [sg.Checkbox('Inverter Vertical', default=True)],[sg.Checkbox('Inverter Horizontal', default=False)],
  
  [sg.Text('Quantidade de fotos'),sg.Spin([i for i in range(1,101)], initial_value=1)],
  
  [sg.Submit('Capturar'), sg.Cancel('Sair')]
]

window = sg.Window('PiPy Camera Manager', layout)

while True:
    event, values = window.read()
    if event in (None, 'Sair'): 
        break
    
#Declarar variáveis de configuração da câmera
    opacidade = values[0]
    nitidez = values[1]
    contraste = values[2]
    brilho = values[3]
    saturacao = values[4]
    iso = values[5]
    exposicao = values[6]
    abertura = values[7]
    inverter_v = values[8]
    inverter_h = values[9]
    quantidade = values[10]
#    quantidade = int(quantidade)
  
#Condicionais para traduzir o botão de espelhamento de imagem
    if inverter_v == True:
      inverter_v = '-vf'
    else:
      inverter_v = ''

    if inverter_h == True:
      inverter_h = '-hf'
    else:
      inverter_h = ''

#Inserindo data à variável utilizada no nome da foto
#    os.system('DATE=$(date +"%Y-%m-%d_%H%M")') ##Integrado à outra linha de código para corrigir bugs na versão buildada
 
#Montando o script para tirar foto de acordo com os parâmetros informados na interface
    i = 0
    while i < quantidade:
        os.system('DATE=$(date +"%Y-%m-%d_%H%M") && raspistill {} {} -op {} -sh {} -co {} -br {} -sa {} -ISO {} -ev {} -ss {}us -t 1 -o /home/pi/photos/$DATE{}.jpg' .format(inverter_v,inverter_h,opacidade,nitidez,contraste,brilho,saturacao,iso,exposicao,abertura,n))
#        print('DATE=$(date +"%Y-%m-%d_%H%M") && raspistill {} {} -op {} -sh {} -co {} -br {} -sa {} -ISO {} -ev {} -ss {}us -t 1 -o /home/pi/photos/$DATE{}.jpg' .format(inverter_v,inverter_h,opacidade,nitidez,contraste,brilho,saturacao,iso,exposicao,abertura,n))
        i+=1
        n+=1
    
window.close()
