from abc   import ABC, abstractmethod
import itertools
import random
from time import sleep
import os

def BaseMachine(ABC):
    @abstractmethod
    def _gen_permutations(self): #combinações possíveis
        ...
    
    @abstractmethod
    def _get_final_result(self):
        ...
    
    @abstractmethod
    def _display(self): #animação das colunas girando
        ...
        
    @abstractmethod
    def _check_result_user(self): #verificação de quem ganhou 
        ...
        
    #aumento de dinheiro do user ou da máquina    
    @abstractmethod
    def _update_balance(self):
        ...
        
    @abstractmethod
    def emojize(self):#transofrmar o codigo em emoji
        ...
        
    @abstractmethod
    def gain(self):
        ...
    
    @abstractmethod
    def play(self, amount_bet, player):
        ...


class player():
    def __init__(self, balance = 0):
        self.balance = balance


class CassaNiquel:
    
    def __init__(self, level = 1, balance = 0):
        self.SIMBOLOS = {
            'smiling_faces': '1F608',
            'skull':'1F480',
            'ghost':'1F47B',
            'heart':'1F495',
            'alien':'1F47D'
        }
        self.level = level
        self.permutations = self._gen_permutations()
        self.balance = balance
        self.initial_balance = self.balance
        
    def _gen_permutations(self):
        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3)) #o product faz as combinações acontecerem e podem ser repetidas
        for j in range(self.level):
            for i in self.SIMBOLOS.keys():
                permutations.append((i,i,i))
        return permutations
        
    def _get_final_result(self):
        if not hasattr(self, 'permutations'):
            self.permutations = self._gen_permutations()    
        
        result = list(random.choice(self.permutations))

        if len(set(result)) == 3 and random.randint(0,5) >= 2:
            result[1] = result [0]
        
        return result

    def _display(self, amount_bet, result, time=0.3):
        seconds = 2
        for i in range(0, int(seconds/time)):
            print(self._emojize(random.choice(self.permutations)))
            sleep(time)
            #os.system('cls')
        print(self._emojize(result))

        if self._check_result_user(result):
            print(f'Você venceu e recebeu: {amount_bet*3}')
        else:
            print('Tente novamente')

    def _emojize(self, emojis):
        return''.join(tuple(chr(int(self.SIMBOLOS[code],16)) for code in emojis))
    

    def _check_result_user(self, result):
        x = [result[0] == x for x in result]
        return True if all(x) else False

    def _update_balance(self, amount_bet, result, player: player):
        if self._check_result_user(result):
            self.balance -= (amount_bet * 3)
            player.balance += (amount_bet*3)
        else:
            self.balance += amount_bet
            player.balance -= amount_bet
    
    def play(self, amount_bet, player: player):
        result = self._get_final_result()
        self._display(amount_bet, result)
        self._update_balance(amount_bet, result, player)

maquina1 = CassaNiquel()
player1 = player()
maquina1.play(100, player1)




