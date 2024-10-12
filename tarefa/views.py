from .models import Tarefa
from .forms import TarefaForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.db.models import Q  


class ListaTarefa(ListView):
    model = Tarefa
    template_name = 'lista.html'
    context_object_name = 'tarefas'

    def get_queryset(self):
       
        query = self.request.GET.get('query')
        if query:
            
            return Tarefa.objects.filter(Q(nome_tarefa__icontains=query))
        else:
            
            return Tarefa.objects.all()

 
class NovaTarefa(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'nova.html'
    success_url = '/lista'


class AtualizarTarefa(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'atualizar.html'
    success_url = '/lista'


class DeletarTarefa(DeleteView):
    model = Tarefa
    template_name = 'deletar.html'
    success_url = '/lista'
