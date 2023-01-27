import PySimpleGUI as sg

class tela:
    def __init__(self):
        sg.change_look_and_feel('BlueMono')
        #Layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais Provedores de e-mail você usa ?')],
            [sg.Checkbox('Gmail', key='Gmail'),sg.Checkbox('Outlook', key='Outlook'),sg.Checkbox('Yahoo', key='Yahoo')],
            [sg.Text('Aceita Cartão')],
            [sg.Radio('Sim','Cartões', key='aceitaCartao'),sg.Radio('Não','Cartões', key='naoaceitaCartao')],
            [sg.Slider(range=(0,255), default_value=(0), orientation='h',size=(15,20),key='Slider_Velocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(50,20))]            
        ]
        #Janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)

    def iniciar(self):
        while True:
            #Extração de dados
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['Gmail']
            aceita_outlook = self.values['Outlook']
            aceita_yahoo = self.values['Yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoaceitaCartao']
            velocidade_script = self.values['Slider_Velocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Outlook: {aceita_outlook}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita Cartão: {aceita_cartao}')
            print(f'Não Aceita Cartão: {nao_aceita_cartao }')
            print(f'Velocidade Script: {velocidade_script}')
        
        
tela = tela()
tela.iniciar()





