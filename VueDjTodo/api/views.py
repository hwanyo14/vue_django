from ast import Delete
from django.http import JsonResponse
from django.views.generic import ListView, DeleteView
from todo.models import Todo
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class ApiTodoLV(ListView):
  model = Todo

  # def get(self, request, *args, **kwargs):
  #   tmpList = [
  #     {'id': 1, 'name': "d김석훈", 'todo': "first item of todoList" },
  #     {'id': 2, 'name': "d홍길동", 'todo': "second item of todoList" },
  #     {'id': 3, 'name': "d이순신", 'todo': "third item of todoList" },
  #     {'id': 4, 'name': "d성춘향", 'todo': "fourth item of todoList" },
  #   ]
  #   return JsonResponse(data=tmpList, safe=False)

  def render_to_response(self, context, **response_kwargs):
    todoList = list(context['object_list'].values())
    return JsonResponse(data=todoList, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ApiTodoDelV(DeleteView):
  model = Todo

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    self.object.delete()
    return JsonResponse(data={}, status=204)