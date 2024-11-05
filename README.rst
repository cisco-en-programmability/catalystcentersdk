=============
catalystcentersdk
=============

*Work with the CatalystCenter APIs in native Python!*

-------------------------------------------------------------------------------

**catalystcentersdk** is a *community developed* Python library for working with the CatalystCenter APIs.  Our goal is to make working with CatalystCenter in Python a *native* and *natural* experience!

.. code-block:: python

    from catalystcentersdk import api

    # Create a CatalystCenterAPI connection object;
    # it uses CatalystCenter sandbox URL, username and password, with CatalystCenter API version 2.3.5.3.
    # and requests to verify the server's TLS certificate with verify=True.
    catalyst = api.CatalystCenterAPI(username="devnetuser",
                            password="Cisco123!",
                            base_url="https://sandboxdnac.cisco.com:443",
                            version='2.3.7.6',
                            verify=True)

    # Find all devices that have 'Switches and Hubs' in their family
    devices = catalyst.devices.get_device_list(family='Switches and Hubs')

    # Print all of demo devices
    for device in devices.response:
        print('{:20s}{}'.format(device.hostname, device.upTime))

    # Find all tags
    all_tags = catalyst.tag.get_tag(sort_by='name', order='des')
    demo_tags = [tag for tag in all_tags.response if 'Demo' in tag.name ]

    #  Delete all of the demo tags
    for tag in demo_tags:
        catalyst.tag.delete_tag(tag.id)
    
    # Create a new demo tag
    demo_tag = catalyst.tag.create_tag(name='catalyst Demo')
    task_demo_tag = catalyst.task.get_task_by_id(task_id=demo_tag.response.taskId)

    if not task_demo_tag.response.isError:
        # Retrieve created tag
        created_tag = catalyst.tag.get_tag(name='catalyst Demo')

        # Update tag
        update_tag = catalyst.tag.update_tag(id=created_tag.response[0].id, 
                                         name='Updated ' + created_tag.response[0].name,
                                         description='DNA demo tag')
        
        print(catalyst.task.get_task_by_id(task_id=update_tag.response.taskId).response.progress)
        
        # Retrieved updated
        updated_tag = catalyst.tag.get_tag(name='Updated catalyst Demo')
        print(updated_tag)
    else:
        # Get task error details 
        print('Unfortunately ', task_demo_tag.response.progress)
        print('Reason: ', task_demo_tag.response.failureReason)

    # Advance usage example using Custom Caller functions
    # Define the get_global_credentials and create_netconf_credentials functions
    # under the custom_caller wrapper.
    # Call them with:
    #     catalyst.custom_caller.get_global_credentials('NETCONF')
    #     catalyst.custom_caller.create_netconf_credentials('65533')
    def setup_custom():
        catalyst.custom_caller.add_api('get_global_credentials',
                                lambda credential_type:
                                    catalyst.custom_caller.call_api(
                                        'GET',
                                        '/dna/intent/api/v1/global-credential',
                                        params={
                                            'credentialSubType': credential_type
                                        }).response
                                )
        catalyst.custom_caller.add_api('create_netconf_credentials',
                                lambda port:
                                    catalyst.custom_caller.call_api(
                                        'POST',
                                        '/dna/intent/api/v1/global-credential/netconf',
                                        json=[{
                                            "netconfPort": port
                                        }])
                                )

    # Add the custom API calls to the connection object under the custom_caller wrapper
    setup_custom()
    # Call the newly added functions
    catalyst.custom_caller.create_netconf_credentials('65533')
    print(catalyst.custom_caller.get_global_credentials('NETCONF'))


Introduction
------------
Check out the complete Introduction_

**catalystcentersdk handles all of this for you:**

+ Reads your CatalystCenter credentials from environment variables.

+ Reads your CatalystCenter API version from environment variable CATALYST_CENTER_VERSION.

+ Controls whether to verify the server's TLS certificate or not according to the verify parameter.

+ Reads your CatalystCenter debug from environment variable CATALYST_CENTER_DEBUG. Boolean.

+ Wraps and represents all CatalystCenter API calls as a simple hierarchical tree of
  native-Python methods

+ If your Python IDE supports **auto-completion** (like `PyCharm_`), you can
  navigate the available methods and object attributes right within your IDE

+ Represents all returned JSON objects as native Python objects - you can
  access all of the object's attributes using native *dot.syntax*

+ **Automatic Rate-Limit Handling**  Sending a lot of requests to CatalystCenter?
  Don't worry; we have you covered.  CatalystCenter will respond with a rate-limit
  response, which will automatically be caught and "handled" for you.

+ **Refresh token** Each time the token becomes invalid, the SDK will generate a new valid token for you.

Installation
------------

Installing and upgrading catalystcentersdk is easy:

**Install via PIP**

.. code-block:: bash

    $ pip install catalystcentersdk

**Upgrading to the latest Version**

.. code-block:: bash

    $ pip install catalystcentersdk --upgrade


Compatibility matrix
--------------------
The following table shows the supported versions.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Cisco CatalystCenter version
     - Python "catalystcentersdk" version
   * - 2.3.7.6
     - 2.3.7.6.X

   

If your SDK is older please consider updating it first.

Documentation
-------------

**Excellent documentation is now available at:**
https://catalystcentersdk.readthedocs.io

Check out the Quickstart_ to dive in and begin using catalystcentersdk.


Release Notes
-------------

Please see the releases_ page for release notes on the incremental functionality and bug fixes incorporated into the published releases.


Questions, Support & Discussion
-------------------------------

catalystcentersdk is a *community developed* and *community supported* project.  If you experience any issues using this package, please report them using the issues_ page.


Contribution
------------

catalystcentersdk_ is a community development projects.  Feedback, thoughts, ideas, and code contributions are welcome!  Please see the `Contributing`_ guide for more information.


Inspiration
------------

This library is inspired by the webexteamssdk_  library


Changelog
---------

All notable changes to this project will be documented in the CHANGELOG_ file.

The development team may make additional name changes as the library evolves with the Cisco CatalystCenter APIs.


*Copyright (c) 2024 Cisco Systems.*

.. _Introduction: https://catalystcentersdk.readthedocs.io/en/latest/api/intro.html
.. _catalystcentersdk.readthedocs.io: https://catalystcentersdk.readthedocs.io
.. _Quickstart: https://catalystcentersdk.readthedocs.io/en/latest/api/quickstart.html
.. _catalystcentersdk: https://github.com/cisco-en-programmability/catalystcentersdk
.. _issues: https://github.com/cisco-en-programmability/catalystcentersdk/issues
.. _pull requests: https://github.com/cisco-en-programmability/catalystcentersdk/pulls
.. _releases: https://github.com/cisco-en-programmability/catalystcentersdk/releases
.. _the repository: catalystcentersdk_
.. _pull request: `pull requests`_
.. _Contributing: https://github.com/cisco-en-programmability/catalystcentersdk/blob/master/docs/contributing.rst
.. _webexteamssdk: https://github.com/CiscoDevNet/webexteamssdk
.. _CHANGELOG: https://github.com/cisco-en-programmability/catalystcentersdk/blob/main/CHANGELOG.md
