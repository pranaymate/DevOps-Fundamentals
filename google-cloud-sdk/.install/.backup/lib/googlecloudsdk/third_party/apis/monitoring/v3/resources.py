# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Resource definitions for cloud platform apis."""

import enum


BASE_URL = 'https://monitoring.googleapis.com/v3/'
DOCS_URL = 'https://cloud.google.com/monitoring/api/'


class Collections(enum.Enum):
  """Collections for all supported apis."""

  PROJECTS = (
      'projects',
      'projects/{projectsId}',
      {},
      [u'projectsId']
  )
  PROJECTS_ALERTPOLICIES = (
      'projects.alertPolicies',
      '{+name}',
      {
          '':
              'projects/{projectsId}/alertPolicies/{alertPoliciesId}',
      },
      [u'name']
  )
  PROJECTS_ALERTPOLICIES_CONDITIONS = (
      'projects.alertPolicies.conditions',
      'projects/{projectsId}/alertPolicies/{alertPoliciesId}/conditions/'
      '{conditionsId}',
      {},
      [u'projectsId', u'alertPoliciesId', u'conditionsId']
  )
  PROJECTS_GROUPS = (
      'projects.groups',
      '{+name}',
      {
          '':
              'projects/{projectsId}/groups/{groupsId}',
      },
      [u'name']
  )
  PROJECTS_METRICDESCRIPTORS = (
      'projects.metricDescriptors',
      '{+name}',
      {
          '':
              'projects/{projectsId}/metricDescriptors/{metricDescriptorsId}',
      },
      [u'name']
  )
  PROJECTS_MONITOREDRESOURCEDESCRIPTORS = (
      'projects.monitoredResourceDescriptors',
      '{+name}',
      {
          '':
              'projects/{projectsId}/monitoredResourceDescriptors/'
              '{monitoredResourceDescriptorsId}',
      },
      [u'name']
  )
  PROJECTS_NOTIFICATIONCHANNELDESCRIPTORS = (
      'projects.notificationChannelDescriptors',
      '{+name}',
      {
          '':
              'projects/{projectsId}/notificationChannelDescriptors/'
              '{notificationChannelDescriptorsId}',
      },
      [u'name']
  )
  PROJECTS_NOTIFICATIONCHANNELS = (
      'projects.notificationChannels',
      '{+name}',
      {
          '':
              'projects/{projectsId}/notificationChannels/'
              '{notificationChannelsId}',
      },
      [u'name']
  )
  PROJECTS_UPTIMECHECKCONFIGS = (
      'projects.uptimeCheckConfigs',
      '{+name}',
      {
          '':
              'projects/{projectsId}/uptimeCheckConfigs/'
              '{uptimeCheckConfigsId}',
      },
      [u'name']
  )

  def __init__(self, collection_name, path, flat_paths, params):
    self.collection_name = collection_name
    self.path = path
    self.flat_paths = flat_paths
    self.params = params
