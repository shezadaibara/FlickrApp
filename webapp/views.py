from django.shortcuts import render_to_response
from django.template.context import RequestContext

import flickrapi

from FlickrApp.settings import FLICKR_API_KEY, DEFAULT_LIMIT


def home(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))


def search(request):
    
    try:
        tags = request.GET.get('tags')
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', DEFAULT_LIMIT)
        content = {'success': True,
                   'page': page,
                   'limit': limit}
        flickr = flickrapi.FlickrAPI(FLICKR_API_KEY)
        
        content['tags'] = tags
        content['photos'] = {}
        places_xml = flickr.places_find(query=tags)
        
        if places_xml.get('stat') == 'ok':
            places = list(places_xml[0])
            pdata = []
            for place in places:
                place = dict(place.items())
                pdata.append(place)
                content['photos'][place.get('woe_id')] = []
                photos_xml = flickr.photos_search(
                                        tags=place.get('woe_name'),
                                        per_page=limit,
                                        page=page,
                                        )
                if photos_xml.get('stat') == 'ok':
                    photos = list(photos_xml[0])
                    for photo in photos:
                        photo = dict(photo.items())
                        photo['image_url'], photo['web_url'] = _get_image_url(photo)
                        content['photos'][place.get('woe_id')].append(photo)
                    if not photos:
                        raise Exception('Could Not find any images for place ')
                else:
                    raise Exception('Sorry, could not send a proper request. Try again later.')
            
            if not places:
                raise Exception('Could not find any place called ')
        else:
            raise Exception('Sorry, could not send a proper request. Try again later')
        
    except Exception as e:
        content['success'] = False
        content['error'] = str(e)
#        print '{}:{}'.format(type(e), str(e))
        
    return render_to_response('search.html', content,
                              context_instance=RequestContext(request))
        

def _get_image_url(photo):
    img_url = 'http://farm{farm}.staticflickr.com/{server}/{id}_{secret}_{size}.jpg'.format(
                                    farm=photo.get('farm'),
                                    server=photo.get('server'),
                                    secret=photo.get('secret'),
                                    id=photo.get('id'),
                                    size='n',
                                    )
    web_url = 'http://www.flickr.com/photos/{user}/{id}'.format(
                                   id=photo.get('id'),
                                   user=photo.get('owner')
                                   )
    return img_url, web_url