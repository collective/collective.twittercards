================================================
collective.twittercards
================================================
Integrate `Twitter Cards <https://dev.twitter.com/cards/overview>`_ to Plone.

Prerequiresites
================================================
- Plone 4 (tested with Plone >= 4.3.x)

Supported card types
================================================
- Summary Card
- Summary Large Image Card
- Photo Card

Roadmap
================================================
Some of the upcoming/in-development features/improvements are:

- All card types (Summary Card with Large Image, Photo Card,
  Gallery Card, App Card, Player Card, Product Card).
- Per content item configurable twitter cards.

Installation
================================================
Buildout
------------------------------------------------
>>> [instance]
>>> eggs +=
>>>     collective.twittercards

ZMI
------------------------------------------------
ZMI -> portal_quickinstaller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- First make sure you have the `collective.z3cform.datagridfield` installed.
- Then choose "collective.twittercards" and install it.

Configuration options
================================================
App control panel can be accessed at
http://your-plone-site.com/@@twittercards-settings

.. image:: _static/01_control_panel.png
    :align: center
