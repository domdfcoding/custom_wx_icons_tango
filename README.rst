==================
wx_icons_tango
==================

.. start short_desc

**Tango icon theme for wxPython 🐍**

.. end short_desc

This package provides a wxPython wxArtProvider class with icons from the Tango Icon Theme.


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/custom-wx-icons-tango/latest?logo=read-the-docs
	:target: https://custom-wx-icons-tango.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/custom_wx_icons_tango/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/domdfcoding/custom_wx_icons_tango/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/custom_wx_icons_tango/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/custom_wx_icons_tango/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/custom_wx_icons_tango/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/custom_wx_icons_tango/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.repo-helper.uk/github/domdfcoding/custom_wx_icons_tango/badge.svg
	:target: https://dependency-dash.repo-helper.uk/github/domdfcoding/custom_wx_icons_tango/
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/custom_wx_icons_tango?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/custom_wx_icons_tango
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/wx_icons_tango
	:target: https://pypi.org/project/wx_icons_tango/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/wx_icons_tango?logo=python&logoColor=white
	:target: https://pypi.org/project/wx_icons_tango/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/wx_icons_tango
	:target: https://pypi.org/project/wx_icons_tango/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/wx_icons_tango
	:target: https://pypi.org/project/wx_icons_tango/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/custom_wx_icons_tango
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/custom_wx_icons_tango
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/custom_wx_icons_tango/v0.1.1
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/custom_wx_icons_tango
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2024
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/wx_icons_tango
	:target: https://pypi.org/project/wx_icons_tango/
	:alt: PyPI - Downloads

.. end shields

Installation
===============

.. start installation

``wx_icons_tango`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install wx_icons_tango

.. end installation

Usage
============

To use ``wx_icons_tango`` in your application:

.. code-block:: python

	# this package
	from wx_icons_tango import wxTangoIconTheme


	class MyApp(wx.App):

		def OnInit(self):
			wx.ArtProvider.Push(wxTangoIconTheme())
			self.frame = TestFrame(None, wx.ID_ANY)
			self.SetTopWindow(self.frame)
			self.frame.Show()
			return True

And then the icons can be accessed through wx.ArtProvider:

.. code-block:: python

	wx.ArtProvider.GetBitmap("document-new", wx.ART_OTHER, wx.Size(48, 48))

Any `FreeDesktop Icon Theme Specification <https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>`_ name can be used.

Currently the ``Client ID`` is not used, so just pass ``wx.ART_OTHER``.
