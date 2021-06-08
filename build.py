import os
import shutil
import platform
from conanfile import IgeConan

def setEnv(name, value):
    if platform.system() == 'Windows':
        os.system(f'set {name}={value}')
    else:
        os.system(f'export {name}={value}')
    os.environ[str(name)] = str(value)

def main():
    setEnv('CONAN_REVISIONS_ENABLED', '1')
    os.system('conan create . ige/test')
    return os.system(f'conan upload {IgeConan.name}/{IgeConan.version}@ige/test --all --remote ige-center --force --confirm')

if __name__ == "__main__":
    main()
