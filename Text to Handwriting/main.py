import pywhatkit as pw
txt = '''
hi my name is shivesh , i am a python developer ,i am 4th year UG student ,
and currently i am doing 100 days of code in twitter with python.

'''
pw.text_to_handwriting(txt,[0,0,138])
print(" DONE ")