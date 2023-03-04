from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily


class pdf_template():
    
    def import_font_ttf(font_name, font_file,
                        font_name_italic=None, font_file_italic=None,
                        font_name_bold=None, font_file_bold=None,
                        font_name_bolditalic=None, font_file_bolditalic=None):
        """
        Function to import a series of fonts to use in Reportlab pdfs.
        

        Parameters
        ----------
        font_name : TYPE STRING 
            DESCRIPTION string containing the name you want to attribute to the font
        font_file : TYPE STRING
            DESCRIPTION. string containing the the ttf file of the font to import
        font_name_italic : TYPE, optional
            DESCRIPTION. The default is None.
        font_file_italic : TYPE, optional
            DESCRIPTION. The default is None.
        font_name_bold : TYPE, optional
            DESCRIPTION. The default is None.
        font_file_bold : TYPE, optional
            DESCRIPTION. The default is None.
        font_name_bolditalic : TYPE, optional
            DESCRIPTION. The default is None.
        font_file_bolditalic : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        """
        pdfmetrics.registerFont(TTFont(font_name, font_file))
        
        if font_name_italic is not None:
            pdfmetrics.registerFont(TTFont(font_name_italic, font_file_italic))
        else:
            pass
        
        if font_name_bold is not None:
            pdfmetrics.registerFont(TTFont(font_name_bold, font_file_bold))
        else:
            pass
        
        if font_name_bolditalic is not None:
            pdfmetrics.registerFont(TTFont(font_name_bolditalic, font_file_bolditalic))
        else:
            pass
        
        registerFontFamily(font_name, 
                   normal=font_name, 
                   bold=font_name_bold, 
                   italic=font_name_italic,
                   boldItalic=font_name_bolditalic)
        
    
    def set_doc_style(font_name, font_name_bold):
        """
        

        Parameters
        ----------
        font_name : STRING
            name of the font imported with import_font_ttf function (should be equal to font_name parameter of this function)
        font_name_bold : STRING
            name of the bold font imported with import_font_ttf function (should be equal to font_name_bold parameter of this function)

        Returns
        -------
        style : list of Reportlab styles for Paragraphs.

        """
        
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify',
                                  alignment=TA_JUSTIFY,
                                  fontName=font_name))
        styles.add(ParagraphStyle(name='HeadingCenter', 
                                  alignment=TA_CENTER, 
                                  fontName=font_name_bold))
        styles.add(ParagraphStyle(name='HeadingLeft', 
                                  fontName=font_name_bold,
                                  fontSize=15))
        styles.add(ParagraphStyle(name='HeadingLeft2', 
                                  fontName=font_name_bold))
        styles.add(ParagraphStyle(name='Title_2', 
                                  alignment=TA_CENTER, 
                                  fontSize=18,
                                  fontName=font_name_bold))
        
        return styles     
