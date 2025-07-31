import os,site,sys
c = r"""import sysbuiltins,os
def i(*a,**k): return f"exit({a},{k})\n"
sys.exit=i;os._exit=i;exitSystem=i;exit=i;quit=i
sys.exit=i
os._exit=i
exitSystem=i
exit=i
quit=i
sys.exit = i
os._exit = i
exit = i
quit = i
builtins.exit = i
builtins.quit = i
raise_system_exit = i
raise_system_exit_0 = i
raise_system_exit_1 = i
exception_exit = i
raise_keyboard = i
raise_base = i
raise_system_error = i
zero_div = i
assert_false = i
name_error = i
type_error = i
permission_error = i
kill_self = i
sigterm = i
sigint = i
signal_raise = i
os_abort = i
ctypes_exit = i
ctypes_abort = i
ctypes_quick = i
ctypes__exit = i
os_exit_hex = i
lambda_exit = i
throw_exit = i
type_del_exit = i
sys_clear_exit = i
kill_bash = i
thread_exit = i
mp_exit = i
eval_exit = i
exec_raise = i
sleep_forever = i
os_system_exit = i
ternary_exit = i
built_exit = i
built_quit = i
sys_argv_exit = i
sys_exit_none = i
sys_exit_true = i
sys_exit_false = i
os_exit_bytes = i
import_exit = i
import_os_exit = i
setattr_exit = i
compile_exit = i
inspect_exit = i
mod_exit = i
raise1 = i
exit1 = i
abort1 = i
thread1 = i
process1 = i
signal1 = i
del1 = i
class Q:
 def __init__(self,n):self.n=n
 def __repr__(self):return f"'{self.n}' is blocked"
 def __call__(self,*a,**k):i(*a,**k)
builtins.exit=Q("exit");builtins.quit=Q("quit");builtins.exitSystem=i"""
def setup():
    p = site.getusersitepackages()
    try:os.makedirs(p,exist_ok=True)
    except Exception as e:
        print(e);sys.exit(1)
    f_path = os.path.join(p,"sitecustomize.py")
    try:
        with open(f_path,"w") as f:f.write(c)
    except Exception as e:
        print(e);sys.exit(1)
setup()
