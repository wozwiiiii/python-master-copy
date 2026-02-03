#导入库
import logging
import os
import pickle
from dotenv import load_dotenv

base = os.path.dirname(__file__)
load_dotenv(os.path.join(base,".env"))

logging.basicConfig(level=logging.INFO,format="%(levelname)s:%(message)s")
student_record = os.getenv("STUDENT_RECORD_FILE")

#定义两个函数

def b_read():
    #opening a file&loading it  打开一份文件并加载它
    if not os.path.exists(student_record):
       logging.warning("File not found)")
       return
    '''if not os.path.exists(student_record):
        logging.warning("File not found")
        return'''
    with open(student_record,"rb") as F:
       student = pickle.load(F)
       logging.info("File opened successfully")
       logging.info("Record in the file are:")
       for i in student:
           logging.info(i)

def b_modify():
#deleting the roll no.entered by user 删除
    if not os.path.exists(student_record):
      logging.warning("File not found")    
      return
    roll_no = int(input("Enter the Roll No.to be deleted:"))
    student = 0
    with open(student_record,"rb") as F:
      student = pickle.load(F)

    with open(student_record,"wb") as F:
      rec = [i for i in student if i[0] != roll_no]
      pickle.dump(rec,F)  

#函数调用
b_read()  
b_modify()