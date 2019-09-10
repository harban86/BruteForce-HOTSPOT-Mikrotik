# This generate dictionary and write to file 

def write_file(file_name,data):
    """
    this function write data to file
    :param data:
    :return:
    """
    with open(file_name, 'a') as x_file:
        x_file.write(data+'\n')

def password(file_name,start,finish):
    count = start
    while count < finish:
       write_file(file_name,str(count))
       count = count + 1

def users(file_name):
    alphabet = ['0','1','2','3','4','5','6','7','8','9']
   for first in alphabet:  
      for second in alphabet:
          for third in alphabet:
              for fourth in alphabet:
                  for fifth in alphabet:
                      for sixth in alphabet:
                          for last in alphabet:                        
                write_file(file_name,str('g'+first+second+third+fourth+fifth+sixth+last))

def run():
    # password('passwords.js',100,1000)
    # users('usernames.txt')
    print ('Good bye')

run()
