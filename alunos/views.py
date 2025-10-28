from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AlunoForm, FaculdadeForm, CursoForm

def inserir_tudo(request):
    
    form_map = {
        'submit_aluno': 
        {
            'form': AlunoForm,
            'success_msg': lambda f: f"Aluno '{f.cleaned_data['nome']}' inserido com sucesso!",
            'is_aluno': True
        },
        'submit_faculdade':
        {
            'form': FaculdadeForm,
            'success_msg': "Faculdade adicionada com sucesso!",
            'is_aluno': False
        },
        'submit_curso': 
        {
            'form': CursoForm,
            'success_msg': "Curso adicionado com sucesso!",
            'is_aluno': False
        },
    }
    

    forms_context ={
        'form_aluno': AlunoForm(),
        'form_faculdade': FaculdadeForm(),
        'form_curso': CursoForm(),
    }

    if request.method == 'POST':
        
        for submit_name, data in form_map.items():
            if submit_name in request.POST:
                
                FormClass = data['form']
                form = FormClass(request.POST)
                
             
                if form.is_valid():
                    form.save()
                    
                    if data['is_aluno']:
                        msg = data['success_msg'](form)
                    else:
                        msg = data['success_msg']
                        
                    messages.success(request, msg)
                    return redirect('inserir_aluno')
                
           
                else:
                  
                    form_key = f"form_{FormClass._meta.model.__name__.lower()}"
                    forms_context[form_key] = form
                    break
        
    return render(request, 'alunos/inserir_aluno.html', forms_context)