from django.shortcuts import render, render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext

@staff_member_required
def myview(request):
    return render_to_response('custom_admin/c_index.html',
                              context=RequestContext(request))
