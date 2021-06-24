"""
Created on Tue Jun 22 17:24:45 2021

@author: hemachandrandhinakaran
"""
from hashlib import new
from os import path
from azureml.core import Workspace, Datastore, Dataset, Experiment

# create workspace
ws = Workspace.create(
    name="Demosdkmlworkspace",
    subscription_id="Your Subscription ID",
    resource_group="demosdkamlRG",
    create_resource_group=True,
    location="eastus2",
)
# write config
ws.write_config(path="/Users/hemz/Documents/GitHub/Machine_Learning/azuremlsdk/")
