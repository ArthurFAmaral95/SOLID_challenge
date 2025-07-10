'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''

#código sem SRP
class TaskHandler:
  def connect_api(self):
    pass

  def create_task(self):
    pass

  def update_task(self):
    pass

  def remove_task(self):
    pass

  def send_notification(self):
    pass

  def generate_report(self):
    pass

  def send_report(self):
    pass

#código com SRP
class ConnectAPI:
  def do_task(self):
    print('API connected')

class CreateTask:
  def do_task(self):
    print('Task created')  

class UpdateTask:
  def do_task(self):
    print('Task updated')

class RemoveTask:
  def do_task(self):
    print('Task removed')

class SendNotification:
  def do_task(self):
    print('Notification sent')

class GenerateReport:
  def do_task(self):
    print('Report generated')

class SendReport:
  def do_task(self):
    print('Report sent')

class TaskHandlerSRP:
  def handle(self, task: any) -> None:
    task.do_task()

connect_api = ConnectAPI()
create_task = CreateTask()
update_task = UpdateTask()
remove_task = RemoveTask()
send_notification = SendNotification()
generate_report = GenerateReport()
send_report = SendReport()
task_handler = TaskHandlerSRP()

task_handler.handle(connect_api)
task_handler.handle(create_task)
task_handler.handle(update_task)
task_handler.handle(remove_task)
task_handler.handle(send_notification)
task_handler.handle(generate_report)
task_handler.handle(send_report)

'''SOLUCAO ROCKETSEAT'''

class TaskHandlerRS:
  def create_task(self):
    pass

  def update_task(self):
    pass

  def remove_task(self):
    pass

class Reports:
  def generate_report(self):
    pass

  def send_report(self):
    pass

class Notification:
  def send_notification(self):
    pass

class ConnectAPIRS:
  def connect_api(self):
    pass