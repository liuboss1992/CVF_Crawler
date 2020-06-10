########################################
# Crawler for CVF Papers
# By Boss Liu: 774054270@qq.com
########################################

import re
import os

def main():
    os.system("wget -q http://openaccess.thecvf.com/CVPR2019.py -O page")
    f = open('./page', 'r')
    data = f.read()
    f.close()   

    key = data
    p1 = r"papers/(\S+)\">pdf</a>"

    pattern1 = re.compile(p1,re.DOTALL)
    match = re.findall(pattern1,key)

    for (i,paper) in enumerate(match):
        print('Downloading the {}th paper: {}'.format(i,paper))
        os.system('wget -q http://openaccess.thecvf.com/content_CVPR_2019/papers/'+ match[i])

    os.system('rm page')

if __name__ == "__main__":
    conferences = ['CVPR 2020','WACV 2020','ICCV 2019','CVPR 2019','CVPR 2018','ICCV 2017','CVPR 2017','CVPR 2016','ICCV 2015','CVPR 2015','CVPR 2014','ICCV 2013','CVPR 2013','ECCV 2018']
    index = input("Choose the Conference You Want:")
    #main()