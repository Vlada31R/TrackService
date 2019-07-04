from django.contrib import admin
from django.contrib import auth
from django.http import HttpResponse
from import_export.admin import ImportExportActionModelAdmin
import csv
from .models import *


class TrackInline(admin.StackedInline):
    model = Tracks.genres.through


@admin.register(Tracks)
class TrackAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("title", "slug", "data_pub",)
    list_filter = ("genres", "data_pub",)
    fields = ('title', 'performer', 'genres',)
    filter_horizontal = ('genres',)
    inlines = [
        TrackInline,
    ]
    actions = ["export_to_csv"]
    
    def export_to_csv(self, request, queryset):
        meta = self.model._meta 
        field_names =  ['id', 'title', 'slug', 'performer', 'data_pub']
        q = [str(i) for i in list(queryset.values_list('id', flat=True))]
        file_name = ';'.join(q)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(file_name)
        writer = csv.writer(response, delimiter='|')
    
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
    
        return response


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    fields = ('title',)


admin.site.site_header = "TrackServiceAdmin"
admin.site.site_title = "TrackServiceAdmin"
