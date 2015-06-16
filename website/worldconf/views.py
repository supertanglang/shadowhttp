#coding: utf8
import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from .models import WorldConf
from .forms import AddWorldConfForm

def update_conf():
    f = open('/etc/dnsmasq.d/world.conf', 'w')
    for d in WorldConf.objects.all():
        f.write('address=/%s/%s\n' % (d.domain, settings.ROUTER_IP))
    f.close()
    os.system('sudo service dnsmasq restart')

# Create your views here.
def world_conf(request):
    form = AddWorldConfForm(request.POST or None)
    if form.is_valid():
        domain = form.cleaned_data['domain']
        try:
            WorldConf.objects.get(domain=domain)
        except:
            WorldConf.objects.create(domain=domain)
        messages.success(request, 'Added domain: %s' % domain)
        update_conf()
        return redirect('world_conf')

    domain_list = WorldConf.objects.order_by('domain')
    return render(request, 'world_conf.html', {'domain_list': domain_list, 'form': form})

def world_conf_del(request, pk):
    w = WorldConf.objects.get(pk=pk)
    w.delete()
    messages.success(request, 'Deleted %s' % w.domain)
    update_conf()
    return redirect('world_conf')

