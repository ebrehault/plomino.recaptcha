# -*- coding: utf-8 -*-
#
# File: text.py
#
# Copyright (c) 2013 by ['Jean Jordaan']
#
# Zope Public License (ZPL)
#

__author__ = """Jean Jordaan <jean.jordaan@gmail.com>"""
__docformat__ = 'plaintext'

from zope.formlib import form
from zope.interface import implements
from zope import component
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from zope.schema import getFields
from zope.schema import Choice
from zope.schema.vocabulary import SimpleVocabulary

try:
    from five.formlib.formbase import EditForm
except:
    #PLONE 3
    from Products.Five.formlib.formbase import EditForm

from Products.CMFPlomino.interfaces import IPlominoField
from Products.CMFPlomino.fields.dictionaryproperty import DictionaryProperty 
from Products.CMFPlomino.fields.base import IBaseField, BaseField

class IRecaptchaField(IBaseField):
    """
    Recaptcha field schema
    """
    # widget = Choice(
    #         vocabulary=SimpleVocabulary.fromItems(
    #             [("Recaptcha", "RECAPTCHA"),]),
    #         title=u'Widget',
    #         description=u'Field rendering',
    #         default="RECAPTCHA",
    #         required=True)

class RecaptchaField(BaseField):
    """
    """
    implements(IRecaptchaField)

    plomino_field_parameters = {
            'interface': IRecaptchaField,
            'label': "Recaptcha",
            }

    read_template = PageTemplateFile('recaptcha_read.pt')
    edit_template = PageTemplateFile('recaptcha_edit.pt')

    def validate(self, submittedValue):
        """
        """
        import pdb; pdb.set_trace()
        errors = self.restrictedTraverse('@@captcha').verify()
        return errors

component.provideUtility(RecaptchaField, IPlominoField, 'RECAPTCHA')

for f in getFields(IRecaptchaField).values():
    setattr(RecaptchaField, f.getName(), DictionaryProperty(f, 'parameters'))

class SettingForm(BaseForm):
    """
    """
    form_fields = form.Fields(IRecaptchaField)

