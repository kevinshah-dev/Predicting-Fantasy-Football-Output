from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from predictions.models import CurrentStat, Team
from django.contrib.auth.models import User

def base(request):
    return render(request, 'base.html')

def search(request):
    query = request.GET['autocomplete']
    response = []
    
    if query:
        players = CurrentStat.objects.filter(name__iregex=r'{0}'.format(query))

        for player in players:
            response.append(player.name)

    return JsonResponse({'status':200, 'data':response})

def home(request):
    context = {}
    
    return render(request, 'home.html', context)

def player(request):
    query = request.GET.get('player', '')
    context = {}
    query_results = CurrentStat.objects.filter(name__iregex=r'{0}'.format(query))

    if len(query_results) == 1:
        context['player'] = [query_results[0]]
        context['fields'] = [{'field_name' : f.verbose_name, 'field': f.name, 'stat': getattr(context['player'][0], f.name)} for f in CurrentStat._meta.get_fields()]
        team = Team.objects.filter(abbreviation = context['player'][0].team)[0]
        context['infobox'] = {
            'team': team.name,
            'logo': team.image,
            'background': team.backgroundImage,
            'headshot': context['player'][0].head_shot
        }

        context['prediction'] = context['player'][0].prediction
        context['error'] = "{:.2f}".format(abs(context['player'][0].points - context['prediction']) * 100 / context['player'][0].points)
        context['prediction'] = "{:.2f}".format(context['prediction'])
        context['exclude_list'] = ['id', 'name', 'team', 'position', 'pos_QB', 'pos_RB', 'pos_TE', 'pos_WR', 'pos_WR_RB', 'pos_WR_TE', 'prediction', 'head_shot']
    elif len(query_results) > 1:
        context['player'] = query_results
    else:
        context['player'] = None
        context['query'] = query
    
    return render(request, 'player.html', context)