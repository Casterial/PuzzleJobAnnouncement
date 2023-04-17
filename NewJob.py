import binascii
import MyLib as my_lib
import codecs
import string

my_dict = dict(enumerate(string.ascii_lowercase, 1))
my_list = []
my_list.extend([my_dict[3],my_dict[18],my_dict[25],my_dict[16],my_dict[20],my_dict[9],my_dict[3]])      

def lifeUpdate(my_list):

    life_update = ''.join(str(x) for x in my_list)
    life_update_hex = life_update.encode('utf-8').hex()
    life_update_bs = codecs.decode(life_update_hex, 'hex')
    
    
    print(str(life_update_bs, 'utf-8'))


if __name__ == "__main__":
    lifeUpdate(my_list)
