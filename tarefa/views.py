from .models import Tarefa
from .forms import TarefaForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.db.models import Q  # Import necessário para buscas complexas

# Listar tarefas com funcionalidade de busca
class ListaTarefa(ListView):
    model = Tarefa
    template_name = 'lista.html'
    context_object_name = 'tarefas'

    def get_queryset(self):
        # Pega o termo de busca da requisição GET
        query = self.request.GET.get('query')
        if query:
            # Se houver uma busca, filtra as tarefas com base no nome
            return Tarefa.objects.filter(Q(nome_tarefa__icontains=query))
        else:
            # Se não houver busca, retorna todas as tarefas
            return Tarefa.objects.all()

# Nova Tarefa 
class NovaTarefa(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'nova.html'
    success_url = '/lista'

# Atualizar Tarefas
class AtualizarTarefa(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'atualizar.html'
    success_url = '/lista'

# Apagar tarefas
class DeletarTarefa(DeleteView):
    model = Tarefa
    template_name = 'deletar.html'
    success_url = '/lista'
