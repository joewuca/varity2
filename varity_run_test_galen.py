import varity
from datetime import datetime
test_file = open('/home/rothlab/jwu/projects/varity/output/log/test_galen.log','w')
msg = 'Galen job is running OK.....'
test_file.write(str(datetime.now())[:19] +'||' + msg + '\n')
test_file.close()