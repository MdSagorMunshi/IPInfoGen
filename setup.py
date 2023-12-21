import os
import sys

script_name = 'IPInfoGen.py'
source_code = open(script_name).read()
path = sys.prefix

if sys.platform.startswith('linux'):
    bin_path = '/usr/local/bin/IPInfoGen'
    lib_path = f'{path}/lib/python{sys.version_info.major}.{sys.version_info.minor}/{script_name}'
    code_bin = f'''#!/usr/bin/env python
from IPInfoGen import main
if __name__ == '__main__':
    main()
'''

elif sys.platform.startswith('win'):
    bin_path = f'{path}/Scripts/IPInfoGen.exe'
    lib_path = f'{path}/Lib/site-packages/IPInfoGen.py'
    code_bin = f'''#!/usr/bin/env python
from IPInfoGen import main
if __name__ == '__main__':
    main()
'''

elif sys.platform.startswith('linux'):
    bin_path = f'{path}/bin/IPInfoGen'
    lib_path = f'{path}/lib/python{sys.version_info.major}.{sys.version_info.minor}/{script_name}'
    code_bin = f'''#!/data/data/com.termux/files/usr/bin/python
from IPInfoGen import main
if __name__ == '__main__':
    main()
'''

else:
    exit('Unsupported platform')

def install_script():
    with open(bin_path, 'w') as handle:
        handle.write(code_bin)
    os.system(f'chmod 775 {bin_path}')
    with open(lib_path, 'w') as handle2:
        handle2.write(source_code)

def uninstall_script():
    try:
        for index_name in (bin_path, lib_path):
            os.unlink(index_name)
    except Exception as e:
        print(f"Error during uninstallation: {e}")

def main():
    argv = sys.argv
    if len(sys.argv) != 2:
        exit('usage: setup.py (install - uninstall)')
    if argv[1] == 'install':
        install_script()
        print("IPInfoGen has been installed successfully.")
    elif argv[1] == 'uninstall':
        uninstall_script()
        print("IPInfoGen has been uninstalled successfully.")
    else:
        exit('usage: setup.py (install - uninstall)')

if __name__ == '__main__':
    main()
