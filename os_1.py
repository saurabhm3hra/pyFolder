import os
import shelve
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='1Log.log')
logging.debug('Start of the Program')
os.makedirs('test_os', exist_ok=True)
os.chdir('./')
print(os.getcwd())
print(os.listdir('./'))

shelfile = shelve.open('mydata')
vari = ['1', '2']
shelfile['vars'] = vari
shelfile.close()
