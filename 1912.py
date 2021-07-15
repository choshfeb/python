import sys
import codecs

w = codecs.getwriter('utf-8')(sys.stdout.buffer)
print('한글', file = w)

#AttributeError: 'StdOutputFile' object has no attribute 'buffer'
#에러 발생
