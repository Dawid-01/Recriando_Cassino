from abc   import ABC, abstractmethod
import itertools
import random
from time import sleep

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

class CassaNiquel:
    
    def __init__(self, level = 1):
        self.SIMBOLOS = {
            'smiling_faces': '1F608',
            'skull':'1F480',
            'ghost':'1F47B',
            'heart':'1F495',
            'alien':'1F47D'
        }
        self.level = level
        self.permutations = self._gen_permutations()
        
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

    def _display(self, amount_bet, result, time=1):
        seconds = 2
        for i in range(0, int(seconds/time)):
            print(self._emojize(random.choice(self.permutations)))
            sleep(time)
        print(self._emojize(result))

    def _emojize(self, emojis):
        return''.join(tuple(chr(int(self.SIMBOLOS[code],16)) for code in emojis))
    

    #def _check_result_user(self, result):



maquina1 = CassaNiquel()
maquina1._display(0,maquina1._get_final_result())