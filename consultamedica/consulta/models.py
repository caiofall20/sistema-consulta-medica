from django.db import models


# Create your models here.
class Medico(models.Model):
	nome = models.CharField(max_length=50)
	crm = models.CharField(max_length=30)
	especialidade = models.CharField(max_length=30)
	def __str__(self):
		return self.nome

class Paciente(models.Model):
	nome = models.CharField(max_length=50)
	cpf_paciente = models.IntegerField()
	data_de_nascimento = models.DateField()
	endereco = models.CharField(max_length=50)
	celular = models.IntegerField()
	telefone_fixo = models.IntegerField()

	def __str__(self):
		return self.nome

class Consulta(models.Model):
	idconsulta = models.IntegerField()
	crm = models.ForeignKey(Medico)
	cpfpaciente = models.ForeignKey(Paciente, null=True)
	horario_inicial = models.DateTimeField(auto_now_add=True, blank=True)
	horario_final = models.DateTimeField(auto_now_add=True, blank=True)
	def __int__(self):
		return self.idconsulta

