from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from consulta.models import Paciente
from consulta.models import Medico
from consulta.models import Consulta
from consulta.forms import ConsultaForm
from consulta.forms import PacienteForm
from consulta.forms import MedicoForm
# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def pacientes(request):
	pacientes = Paciente.objects.all()
	teste = 'Pacientes'
	template = loader.get_template('pacientes.html')
	context = RequestContext(request,{'pacientes':pacientes})
	return HttpResponse(template.render(context))

def medicos(request):
	medicos = Medico.objects.all()
	teste = 'Medicos'
	template = loader.get_template('medicos.html')
	context = RequestContext(request,{'medicos':medicos})
	return HttpResponse(template.render(context))

def consultas(request):
	consultas = Consulta.objects.all()
	teste = 'Consultas'
	template = loader.get_template('consultas.html')
	context = RequestContext(request,{'consultas':consultas})
	return HttpResponse(template.render(context))

def model_forms(request):
	form = ConsultaForm(request.POST or None)

	if request.method == 'POST':
		form.save()

	template = loader.get_template('cadastro-consultas.html')
	return render(request, 'cadastro-consultas.html', {'form':form})

def paciente_forms(request):
	form = PacienteForm(request.POST or None)

	if request.method == 'POST':
		form.save()

	template = loader.get_template('cadastro-paciente.html')
	return render(request,'cadastro-paciente.html', {'form':form})

def medico_forms(request):
	form = MedicoForm(request.POST or None)

	if request.method == 'POST':
		form.save()

	template = loader.get_template('cadastro-medico.html')
	return render(request,'cadastro-medico.html', {'form':form})