# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 01:23:41 2025

@author: Hairton Rafael Chalco lima
"""
from pyautocad import Autocad, APoint

class AutoCADManager:
    def __init__(self, offset=10, text_height=2.5):
        self.acad = Autocad()
        self.configure_autocad()
        self.offset = offset
        self.text_height = text_height
        
    def configure_autocad(self):
        self.acad.doc.SendCommand("PDMODE 35 ")
        self.acad.doc.SendCommand("PDSIZE 5 ")
    
    def draw_point(self, x, y, text):
        point = APoint(x, y)
        self.acad.model.AddPoint(point)
        text_position = APoint(x + self.offset, y)
        self.acad.model.AddText(text, text_position, self.text_height)

