"""URL patterns for Bathynomus - root level"""
from django.urls import path, include

from Bathynomus.views.application.application_views import ApplicationView

urlpatterns = [
    # Fallback urls to the frontend
    path("<path:_>", ApplicationView.as_view(), name="application"),
    path("", ApplicationView.as_view(), name="application"),
]


"""
NOTES
~~~~~

-- PROJECT --
/api/v1/project
/api/v1/project/<project_id>
/api/v1/project/<project_id>/requirement
/api/v1/project/<project_id>/requirement/<requirement_id>

-- PROJECT TEST RUN --
/api/v1/project/<project_id>/test_run
/api/v1/project/<project_id>/test_run/<test_run_id>
/api/v1/project/<project_id>/test_run/<test_run_id>/test_case_result
/api/v1/project/<project_id>/test_run/<test_run_id>/test_case_result/<test_case_result_id>


** Tests can be shared between projects, so we don't need to specify the project_id ** 
-- FOLDER --
/api/v1/folder
/api/v1/folder/<folder_id>

-- PROJECT TEST CASE --
/api/v1/test_case
/api/v1/test_case/<test_case_id>


"""