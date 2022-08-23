from django.db import models

# Create your models here.

class login(models.Model):
    usuario = models.CharField('Nome de Usuário', max_length=20)
    senha = models.CharField('Senha', max_length=20)

class reserva(models.Model):
    setor = models.CharField('Setor',max_length=20)
    solicitante = models.CharField('Solicitante', max_length=20)
    data_solicitacao = models.DateField('Data da Solicitação')
    data_agenda = models.DateField('Data de agendamento')
    chamado_GLPI = models.CharField('Chamado GLPI', max_length=10)
    hora_inicio = models.TimeField('Inicio da Reserva')
    hora_final = models.TimeField('Final da Reserva')
    observacao = models.CharField('Observação', max_length=100)
