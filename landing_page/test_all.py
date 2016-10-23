import sys, os
from application.settings import *

sys.path.append(os.path.join(BASE_DIR, 'landing_page/tests'))


from test_landing_page_admin import *
from test_landing_page_views import *
