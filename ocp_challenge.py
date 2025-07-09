'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''

#código sem OCP
class AprovaExame:
  def aprovar_solicitacao_exame(self, exame):
    if exame.tipo == 'sangue':
      if aprovador.verifica_condicoes_exame_sangue(exame):
        print('Exame de sangue aprovado')
    
    elif exame.tipo == 'raio-x':
      if aprovador.verifica_condicoes_raio_x(exame):
        print('Raio-X aprovado')
        pass

  def verifica_condicoes_exame_sangue(self, exame):
    return True

  def verifica_condicoes_raio_x(self,exame):
    return True


class Exame:
  def __init__(self, tipo: str):
    self.tipo = tipo


exame_sangue = Exame('sangue')
exame_raio_x = Exame('raio-x')

aprovador = AprovaExame()

aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)