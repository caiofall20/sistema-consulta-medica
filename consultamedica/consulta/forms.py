from django import forms
from django.forms import ModelForm
from consulta.models import *

class ConsultaForm(ModelForm):
	class Meta:
		model = Consulta
		fields = ['idconsulta','crm','cpfpaciente']

class PacienteForm(ModelForm):
	class Meta:
		model = Paciente
		fields = ['nome', 'cpf_paciente','data_de_nascimento','endereco','celular','telefone_fixo']

class MedicoForm(ModelForm):
	class Meta:
		model = Medico
		fields = ['nome','crm','especialidade']
