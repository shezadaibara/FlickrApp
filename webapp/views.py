from django.shortcuts import render_to_response
from django.template.context import RequestContext
import flickrapi

from FlickrApp.settings import FLICKR_API_KEY


def home(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))


def search(request):
    try:
        tags = request.POST.get('tags')
        content = {'success': True}
        flickr = flickrapi.FlickrAPI(FLICKR_API_KEY)
        
        content['tags'] = tags
        content['photos'] = {}
        data = flickr.places_find(query=tags)
        
        if data.get('stat') == 'ok':
            places = list(data[0])
            for place in places:
                print place.keys()
            
        else:
            raise Exception('Could not find the place')
        print content
    except Exception as e:
        content['success'] = False
        content['error'] = type(e) + ':' + str(e)
        
        
    return render_to_response('search.html',
                              context_instance=RequestContext(request))
        

