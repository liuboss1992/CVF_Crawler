########################################
# Crawler for CVF Papers
# By Boss Liu: 774054270@qq.com
########################################

import re
import os

def cvf_spider(conference):
    py_conference = conference.replace(' ','')
    #print(py_conference)
    folder_conference = conference.replace(' ','_')
    #print(folder_conference)

    os.system("wget -q http://openaccess.thecvf.com/"+py_conference+".py -O page")
    f = open('./page', 'r')
    data = f.read()
    f.close()   

    key = data
    p1 = r"papers/(\S+)\">pdf</a>"

    pattern1 = re.compile(p1,re.DOTALL)
    match = re.findall(pattern1,key)

    folder = os.path.exists('./'+py_conference)
    if not folder:
        os.makedirs('./'+py_conference)

    for (i,paper) in enumerate(match):
        print('Downloading the {}th paper: {}'.format(i,paper))
        #os.system('wget -q http://openaccess.thecvf.com/content_CVPR_2019/papers/'+ match[i])

    os.system('rm page')


if __name__ == "__main__":
    conferences = ['CVPR 2020','WACV 2020','ICCV 2019','CVPR 2019','CVPR 2018','ICCV 2017','CVPR 2017','CVPR 2016','ICCV 2015','CVPR 2015','CVPR 2014','ICCV 2013','CVPR 2013','ECCV 2018']
    for (i,paper) in enumerate(conferences):
        print('Index {}: {}'.format(i+1,paper))
    index = input("Choose the Conference You Want, Print 0 to exit: ")
    index = int(index)
    if index == 0:
        print('Exit')
    else:
        conference = conferences[index-1]
        print('You choose to crawler {}, print 1/0 to continue/exit.'.format(conference))

        y_n = input()
        if y_n == 0:
            print('Exit')
        else:
            print('Now Download Papers in {}'.format(conference))
            
            cvf_spider(conference)
    print('All Papers Downloaded!')