from zope import interface
from zope import component

import interfaces

def get_skin_template(context, request, name):
    gsm = component.getSiteManager()
    return gsm.adapters.lookup(
        map(interface.providedBy, (context, request)),
        interfaces.ISkinTemplate, name=name)