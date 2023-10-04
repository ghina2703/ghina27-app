from django.urls import path
# new impor tugas 3
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
# new impor tugas 4
from main.views import register, login_user, logout_user #sesuaikan dengan nama fungsi yang dibuat
from main.views import add_item, reduce_item, delete_item
# new impor tugas 5
from main.views import edit_item
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    # new path tugas 3
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    # new path tugas 4
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'),
    path('add_item/<int:id>/', add_item, name='add_item'),
    path('reduce_item/<int:id>/', reduce_item, name='reduce_item'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'),
    # new path tugas 5
    path('edit-item/<int:id>', edit_item, name='edit_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
