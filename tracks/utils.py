from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Permission


class DetailMixin:
    model = None
    template = None

    @method_decorator(login_required(login_url='login'))
    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template,
                      context={self.model.__name__.lower(): obj,
                               'admin_object': obj,
                               'admin_panel_UD': True})


class ObjectCreateMixin:
    model = None
    template = None

    @method_decorator(login_required)
    def get(self, request):
        form = self.model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model(request.POST, request.FILES)

        if bound_form.is_valid():
            new_object = bound_form.save()
            new_object.user = request.user
            new_object.save()
            return redirect(new_object)
        return render(request, self.template,
                      context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    template = None
    model_form = None

    @method_decorator(login_required)
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template,
                      context={'form': bound_form,
                               self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        return render(request, self.template,
                      context={'form': bound_form,
                               self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    @method_decorator(login_required)
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template,
                      context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
