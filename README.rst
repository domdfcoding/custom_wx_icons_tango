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
	  - |travis| |actions_windows| |actions_macos| |codefactor| |pre_commit_ci|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| image:: https://img.shields.io/readthedocs/custom_wx_icons_tango/latest?logo=read-the-docs
	:target: https://custom_wx_icons_tango.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/custom_wx_icons_tango/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |travis| image:: https://github.com/domdfcoding/custom_wx_icons_tango/workflows/Linux%20Tests/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/actions?query=workflow%3A%22Linux+Tests%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/custom_wx_icons_tango/workflows/Windows%20Tests/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/actions?query=workflow%3A%22Windows+Tests%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/custom_wx_icons_tango/workflows/macOS%20Tests/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_tango/actions?query=workflow%3A%22macOS+Tests%22
	:alt: macOS Test Status

.. |requires| image:: https://requires.io/github/domdfcoding/custom_wx_icons_tango/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/custom_wx_icons_tango/requirements/?branch=master
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

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. |pre_commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
	:target: https://github.com/pre-commit/pre-commit
	:alt: pre-commit

.. |pre_commit_ci| image:: https://results.pre-commit.ci/badge/github/domdfcoding/custom_wx_icons_tango/master.svg
	:target: https://results.pre-commit.ci/latest/github/domdfcoding/custom_wx_icons_tango/master
	:alt: pre-commit.ci status

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

	wx.ArtProvider.GetBitmap('document-new', wx.ART_OTHER, wx.Size(48, 48))

Any `FreeDesktop Icon Theme Specification <https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>`_ name can be used.

Currently the `Client ID` is not used, so just pass `wx.ART_OTHER`.
