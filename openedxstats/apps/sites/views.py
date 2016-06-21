from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Site, SiteLanguage, SiteGeoZone
from .forms import SiteForm

class ListView(generic.ListView):
    model = Site

    template_name = 'sites/sites_list.html'
    context_object_name = 'sites_list'

    #def get_queryset(self):
    #    return Site.objects.all()


# TODO: Implement updating sites, not just adding. Refer to http://www.ianrolfe.com/page/django-many-to-many-tables-and-forms/ for help
def add_site(request):
    # This is where I will add an if statement to check if we are passing in an existing id or making a new object
    # For now, we will just make a new object
    s = Site()

    if request.method == 'POST':
        form = SiteForm(request.POST, instance=s)
        if form.is_valid():
            languages = form.cleaned_data.pop('language')
            geozones = form.cleaned_data.pop('geography')
            form.save()

            # site.language.clear()    # delete existing languages (for when I implment update)
            for l in languages:
                site_language = SiteLanguage.objects.create(language=l, site=s)
                site_language.save()

            for g in geozones:
                site_geozone = SiteGeoZone.objects.create(geo_zone=g, site=s)
                site_geozone.save()

            return HttpResponseRedirect(reverse('sites:sites_list'))
    else:
        form = SiteForm()

    return render(request, 'add_site.html', {'form':form})
