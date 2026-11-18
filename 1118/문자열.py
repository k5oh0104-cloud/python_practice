name = '홍길동'
status = "정상"
code = 'EQP-001'
print('name, status, code:', name, status, code)
sentence = "It's normal"
print('sentence:', sentence)
sentence2 = 'The equipment is "normal"'
print('sentence2:', sentence2) 

sentence3 = "equipment 1 is \"normal\", and equipment2 is \"abnormal\""
print('sentence3:', sentence3)
sentence4 = 'equipment 1 is \'normal\', and equipment2 is \'abnormal\''
print('sentence4:', sentence4)

# test = "writing
# in multiple lines
# creates error"
triple_quote1 = """writing
in multiple lines  
creates no error"""
print('triple_quote1:', triple_quote1)

# escape characters \n, \t, \\, \', \", \r, \b, \f, \v

guide = "This is a guide\nfor using escape characters.\n\n"
print('\n','guide:', guide)
print("what")
print("name",'\t', "status")
print("eqp1",'\t', "normal")

print('C:\\Users\\hpaed\\OneDrive\\바탕 화면\\데이터분석 5기')
print("\\")
print("2025", "01", "01", sep="-")
