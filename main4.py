import os
os.system('clear')
try:
    __import__("shutil").rmtree(dir)
except:
    pass
Black = '\033[0;30m'        
Red = '\033[0;31m'       
Green = '\033[0;32m'       
Yellow = '\033[0;33m'     
Blue = '\033[0;34m'         
purple = '\033[0;35m'    
Cyan = '\033[0;36m'        
White = '\033[0;37m'

import sys
__pypath__ = __import__('os').getcwd()

pyver = ".".join(sys.version.split(" ")[0].split(".")[:-1])

while 1:
    try:
        file = input("\n Path File : ").replace("\"","")
        target = open(file, 'rb').read(4)
        if b"\r\r\n" in target:
            binary = True
        else:
            binary = False
        if int(__import__('os').stat(file).st_size) > 524288000:
            print(' File is Big')
            continue
        break
    except FileNotFoundError:
        print(' File Not Fond')
    except PermissionError:
        print('Erorr')
    except OSError:
        continue

while 1:
    inp = str("1")
    if inp.upper() == "1":
        save_as = True
        break
    elif inp.upper() == "2":
        save_as = False
        break
print()
del inp
data = open(file,'rb').read()

code_dump = ""

if binary:
    for i in range(1,31):
        try:
            if "<code object <module> at " in str(__import__('marshal').loads(data[i:])):
                code_dump = data[i:]
                break
        except:
            continue
else:
    code_dump = data
    data = ''

if not code_dump:
    print("The Tool Not Obf")
    __import__('sys').exit(1)

list_random = []

def random_str(length = 24):
    global list_random
    while 1:
        rand = __import__('random').choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") + "".join([__import__('random').choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0987654321") for i in range(length)])
        if rand in list_random:
            continue
        break
    list_random.append(rand)
    return rand

open('Sajad_Obf.py','w').write(r'exec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(' + str(__import__("base64").b64encode(__import__("zlib").compress(__import__('marshal').dumps(compile(r'''
from builtins import *
from zlib import decompress as {11}
def {10}(id="https://t.me/f_g_d_6"):
    return "# Decode Hard By Sajad\n# Tool name : [{0}] ({1} - {2})\n# dump -> code " + str(id) + "\n\n"
try:
    {6}=exec
    __file__ = """{5}"""
    {7} = 0
    {8} = "w"
    {9} = ""
except:
    __import__('sys').exit(1)
else:
    pass
finally:
    pass
def exec(source,glba=None,lcb=None):
    try:
        global {7}
        if {7}>0:
            pass
        else:
            if not {4}:
                globals()[{11}(b'1\x02x\x06\x00\x01-(+\xcc\xcb\x9cx'[::-1]).decode()]({11}(b'x\x9cSPTT\xf0\xcc+(-QP*N,KUR(\xc9W\x001\x14J2R\x15\x92\xf3SR\x15t\x15\x02\x8aR\x8b\x8b\x15\\\xf3JR\x8b\xc0\xd2\xa9\xa9\ny\xa9\x15%\x10iEE\x00\xce\x05\x15\x88').decode())
            else:
                globals()[{11}(b'1\x02x\x06\x00\x01-(+\xcc\xcb\x9cx'[::-1]).decode()]({11}(b'x\x9cSTT\x08(J-.Vp\xcd+I-R(\xc9W(.I,*Qp,\x051\x13\xcbR\x15\x12sr\x14\x14\x15\x01\r\xd3\r"').decode())
        if source:
            globals()[{11}(b'.\x02\x88\x06\x00\x01+\xcc\xca(+\x9cx'[::-1]).decode()]("\n".format({7}))
            if {11}(b'x\x9c\xb3I\xceOIU\xc8O\xcaJM.Q\xb0\xc9\xcdO)\xcdI\xb5SH,Q\x00\x00s\x0b\x08\xa4').decode() in str(source):
                {8} = "w"
                {9} = {10}({7}) + "exec(__import__('marshal').loads(" + str(__import__('marshal').dumps(source)) + "))\n"
                if not {4}:
                    globals()[{11}(b'.\x02\x88\x06\x00\x01+\xcc\xca(+\x9cx'[::-1]).decode()]({9})
            else:
                {8} = "wb"
                try:
                    {9} = {10}({7}) + source
                except TypeError:
                    {9} = {10}({7}).encode('utf8') + source
                if not {4}:
                    globals()[{11}(b'.\x02\x88\x06\x00\x01+\xcc\xca(+\x9cx'[::-1]).decode()]({9})
                try:
                    {9} = {9}.encode('utf8')
                except:
                    pass
            if not {4}:
                globals()[{11}(b'.\x02\x88\x06\x00\x01+\xcc\xca(+\x9cx'[::-1]).decode()]("\n\n\n")
            if not {4}:
                if globals()[{11}(b'1\x02x\x06\x00\x01-(+\xcc\xcb\x9cx'[::-1]).decode()](' >> "save" or Enter? [Ctrl + C to Exit]: ').lower()=="save":
                    while 1:
                        try:
                            open(globals()[{11}(b'1\x02x\x06\x00\x01-(+\xcc\xcb\x9cx'[::-1]).decode()](' >> file name: '), {8}).write({9})
                            break
                        except KeyboardInterrupt:
                            __import__('os').unlink(r'{3}/Sajad_Obf.py')
                            __import__('sys').exit(0)
                        except:
                            globals()[{11}(b'.\x02\x88\x06\x00\x01+\xcc\xca(+\x9cx'[::-1]).decode()]("!! something is error !!")
                            pass
                    if globals()[{11}(b'1\x02x\x06\x00\x01-(+\xcc\xcb\x9cx'[::-1]).decode()]({11}(b'x\x9c\xb3\xb3Sp\xc9W\xa8\xcc/U(O\xcc+Q(\xc9WH\xce\xcf+\xc9\xcc+M\xb5W\x88\x8e\xd4\xcf\x8b\xb5R\x00\x00\xd0\xb3\x0b\x96').decode()).lower()=="y":
                        pass
                    else:
                        __import__('os').unlink(r'{3}/Sajad_Obf.py')
                        __import__('sys').exit(0)
            else:
                import os; os.makedirs('/storage/emulated/0/DeCoDe_OBF', exist_ok=True)

                open('DeCoDe_OBF/DeCoDe_SaJoDe.py'.format({7}), {8}).write({9})
                globals()[{11}(b'.\x02\x88\x06\x00\x01+\xcc\xca(+\x9cx'[::-1]).decode()](" > Saved: [DeCoDe_OBF/DeCoDe_SaJoDe.py]".format({7}))
                __import__('sys').exit(0)
    except KeyboardInterrupt:
        __import__('os').unlink(r'{3}/Sajad_Obf.py')
        __import__('sys').exit(0)

    {7}+=1
    globals()[{11}(b'.\x02\x88\x06\x00\x01+\xcc\xca(+\x9cx'[::-1]).decode()]({11}(b'x\x9cS\xb0\xb3S\x08O\xcc,\xc9\xccK\xd7\x03\x02\x00"\x13\x04H').decode())
    {6}(source,globals())
from builtins import __import__ as __import__
from builtins import __build_class__ as __build_class__
from builtins import __spec__ as __spec__
'''.format(
        "/".join(file.split("\\")).split("/")[-1],
        str('pyc' if binary else 'py'),
        pyver,
        __pypath__,
        int(save_as),
        "{}".format("/".join(file.split("\\")).split("/")[-1]),
        random_str(),
        random_str(),
        random_str(),
        random_str(),
        random_str(),
        random_str(),
    ),'<Sajad_Obf>','exec'))))[::-1]) + r"[::-1]))),globals())")

if save_as:
    try:__import__('os').mkdir("/".join(file.split("\\")).split("/")[-1] + "_dump")
    except:pass

try:__import__('os').chdir(__import__('os').path.dirname(file))
except:pass

__file__="{}".format("/".join(file.split("\\")).split("/")[-1])
__name__='__main__'
sys.argv[0]=__file__

marshal=r'''
try:
    __import__('Sajad_Obf').__spec__ = __import__('builtins').__spec__
    __import__('sys').modules['builtins']=__import__('sys').modules['Sajad_Obf']
    __import__('builtins').exec.__name__ = 'exec'
    __import__('builtins').exec.__module__ = 'builtins'
    __builtins__ = __import__('builtins')
except:
    __import__('os').unlink(r'{}/Sajad_Obf.py')
    __import__('sys').exit(1)
'''.format(__pypath__).encode('utf8')

if data:
    marshal+=br'''exec(__import__("marshal").loads(''' + str(code_dump).encode() + b"""),globals())"""
else:
    marshal+=code_dump

marshal+="""\n\n__import__('os').unlink(r'{}/Sajad_Obf.py')""".format(__pypath__).encode('utf8')

try:
    del random_str, list_random, data, code_dump, save_as, binary, target, file, pyver
except:
    pass

try:
    exec('exec(__import__("marshal").loads(' + str(__import__('marshal').dumps(compile(marshal, '<Sajad_Obf>', 'exec'))) + "), globals())",globals())
except KeyboardInterrupt:
    pass
except Exception as e:
    __import__('logging').error(__import__('traceback').format_exc())
except:
    pass
try:
    __import__("shutil").rmtree(r'{}/__pycache__'.format(__pypath__))
except:
    pass
try:
    __import__('os').unlink(r'{}/Sajad_Obf.py'.format(__pypath__))
except:
    pass
__import__('sys').exit()
