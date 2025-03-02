from django.urls import path
from .views.MainView import MainView
from .views.UserView import UserView
from .views.GoalView import GoalView
from .views.PhysicalLevelView import PhysicalLevelView
from .views.BodyTypeView import BodyTypeView
from .views.SexTypeView import SexTypeView
from .views.TrainingTypeView import TrainingTypeView

urlpatterns = [
    path("main/", MainView.as_view(), name="main"),
    path("user/data/", UserView.as_view(), name="user"),

    # get data from dictionaries
    path("goals/data/", GoalView.as_view(), name="goals"),
    path("physical_levels/data/",
         PhysicalLevelView.as_view(), name="physical_levels"),
    path("body_types/data/", BodyTypeView.as_view(), name="body_types"),
    path("sex_types/data/", SexTypeView.as_view(), name="sex_types"),
    path("training_types/data/", TrainingTypeView.as_view(), name="training_types"),
]
