
import PyPDF2
import re
import pandas as pd

def read_pdf_document(filepath, begin_page=0, end_page=-1) -> str:
    pdfFileObj = open(filepath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    end_page = end_page if end_page > 0 else pdfReader.numPages
    
    
    pages = ''
    for i in range (begin_page, end_page):
        pageObj = pdfReader.getPage(i)
        pages += ' ' + pageObj.extractText()
    
    text = pages.replace(' -','-')

    #clean up errant situations where two strings are merged without a space
    text = re.sub(r'([a-z])([A-Z])', r'\1. \2', text)
    
    return pages

def split_to_paragraphs(text, file='', limit=100):
    #The limit is a somewhat arbitrary value intented to determine
    #whether newlines are being truly used for paragraph construction
    #or a formatting artifact of the PDF. the value of the limit
    #represents the cutoff for the ratio of newlines to other chars
    #so 100 means if 1% or more of the chars are newlines, we can
    #safely assume newlines are being used for formatting
    
    
    #clean up errant situations where two strings are merged without a space
    text = re.sub(r'([a-z])([A-Z])', r'\1. \2', text)
    
    
    # determine if newlines are used solely in the separation of paragraphs
    # or as is common with pdf, also used to format line-lengths

    chars_per_newline = len(text) / len(text.split('\n')) 
    if chars_per_newline < limit:
        #print('excess_newlines')
        #split the doc on sentence terminators followed by newline
        paragraphs = re.split('[.?!]\s*\n', text)
    else:
        #print('normal_newlines')
        paragraphs = re.split("\s{2,}", text)
        
    #strip out any remaining newlines
    for i in range(len(paragraphs)):
        paragraphs[i] = paragraphs[i].replace('\n',' ')

    #create a dataframe with each paragraph as its own record
    df_paragraphs = pd.DataFrame([{"file" : file, "paragraph" : paragraph}
                             for paragraph in paragraphs if paragraph])
    
    return df_paragraphs

def load_pdf_to_df(file):
    return split_to_paragraphs(read_pdf_document(file), file)



if __name__ == '__main__':
    print('todo: add assertions for testing here')