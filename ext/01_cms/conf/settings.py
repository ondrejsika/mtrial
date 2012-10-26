INSTALLED_APPS += ( 'cms', 'mptt', 'menus', 'sekizai', 'south',  'cms.plugins.file', 'cms.plugins.flash', 'cms.plugins.googlemap', 'cms.plugins.link', 'cms.plugins.picture', 'cms.plugins.snippet', 'cms.plugins.teaser', 'cms.plugins.text', 'cms.plugins.video', 'cms.plugins.twitter',)
MIDDLEWARE_CLASSES += ( 'cms.middleware.multilingual.MultilingualURLMiddleware', 'cms.middleware.page.CurrentPageMiddleware', 'cms.middleware.user.CurrentUserMiddleware', 'cms.middleware.toolbar.ToolbarMiddleware', )
TEMPLATE_CONTEXT_PROCESSORS += ( 'cms.context_processors.media', 'sekizai.context_processors.sekizai', )
CMS_TEMPLATES = ( ('cms/blank.html', 'Blank template'), ('cms/blank_with_menu.html', 'Blank template with menu'), )
LANGUAGES = [ ('en', 'English'), ]
INSTALLED_APPS.remove("django.contrib.flatpages")