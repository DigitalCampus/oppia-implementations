

def modify(settings):
    
    settings['INSTALLED_APPS'] += ('tastypie','sorl.thumbnail',)
    
    settings['THUMBNAIL_COLORSPACE'] = None
    settings['THUMBNAIL_PRESERVE_FORMAT'] = True