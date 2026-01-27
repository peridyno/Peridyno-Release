'''
Author: unibeam98 beyondevery@live.com
Date: 2025-02-21 15:54:24
LastEditors: unibeam98 beyondevery@live.com
LastEditTime: 2025-07-30 17:16:14
FilePath: \PyPeridyno-package\setup.py
Description: Package PyPeridyno
'''
import tempfile
import urllib.request
import zipfile

import setuptools
from setuptools import setup, find_packages, Extension
from setuptools.command.install import install
import os
import sys
import glob
import shutil


def copyData():
    try:
        # copy data
        os.makedirs('C:/ProgramData/Peridyno/data/font', exist_ok=True)
        font_dir = os.getcwd()
        source_path = os.path.join(font_dir, 'src/font')
        destination_path = 'C:/ProgramData/Peridyno/data/font'
        shutil.copytree(source_path, destination_path, dirs_exist_ok=True)

        # copy example
        # os.makedirs('C:/ProgramData/Peridyno/data/example', exist_ok=True)
        # example_dir = os.getcwd()
        # source_path = os.path.join(example_dir, 'src/example/')
        # destination_path = 'C:/ProgramData/Peridyno/data/example'
        # shutil.copytree(source_path, destination_path, dirs_exist_ok=True)

        return True
    except PermissionError as e:
        print(f"Permission denied: {e}")
        print("Please run as administrator or check file permissions")
        return False
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return False
    except OSError as e:
        print(f"OS error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error during data copy: {e}")
        return False

def copyCufft():
    try:
        # copy cufft
        cuda_path = os.getenv('CUDA_PATH')
        # 如果CUDA_PATH环境变量没有被设置，则退出脚本
        if cuda_path is None:
            print("CUDA_PATH 环境变量未设置")
            return False
        cuda_path_bin = cuda_path + '\\bin'
        cuda_path_lib = cuda_path + '\\lib\\x64'
        python_install_path = sys.prefix
        cufft_file_dll = [f for f in os.listdir(cuda_path_bin) if 'cufft' in f]
        cufft_file_lib = [f for f in os.listdir(cuda_path_lib) if 'cufft' in f]
        for file in cufft_file_dll:
            shutil.copy(os.path.join(cuda_path_bin, file), python_install_path)
            print(os.path.join(cuda_path_bin, file))

        for file in cufft_file_lib:
            shutil.copy(os.path.join(cuda_path_lib, file), python_install_path)
            print(os.path.join(cuda_path_lib, file))

        return True
    except Exception as e:
        print(f"Unexpected error during data copy: {e}")
        return False



def checkQt():
    try:
        path_env = os.environ.get('PATH', '')
        qt_paths = []

        for path in path_env.split(';'):
            if 'Qt' in path and ('bin' in path or 'Tools' in path):
                qt_paths.append(path)

        if qt_paths:
            print(qt_paths)
            return True

    except Exception as e:
        print(f"Unexpected error during data copy: {e}")
        return False

def downloadExtract(zipUrl):
    try:
        with tempfile.TemporaryDirectory() as tempDir:
            zipPath = os.path.join(tempDir, "download.zip")
            print(f"Downloading from {zipUrl} to {zipPath}...")

            # download
            urllib.request.urlretrieve(zipUrl, zipPath)
            print("Download completed. Extracting...")

            # 解压文件
            with zipfile.ZipFile(zipPath, 'r') as zip_ref:
                # 获取 Python 安装目录
                python_dir = sys.prefix
                extract_path = python_dir

                print(f"Extracting to: {extract_path}")

                # 解压所有文件
                zip_ref.extractall(extract_path)

            print("Extraction completed successfully!")
            return True
    except Exception as e:
            print(f"Error during download and extraction: {e}")
            return False
    
def extractLocal(zipPath):
    try:
        print(f"Extracting from local path: {zipPath}...")
        with zipfile.ZipFile(zipPath, 'r') as zip_ref:
            python_dir = sys.prefix
            extract_path = python_dir

            print(f"Extracting to {extract_path}")

            zip_ref.extractall(extract_path)

        print("Local extraction complete successful!")
        return True
    except Exception as e:
        print(f"Error during local extraction: {e}")
        return False

class CustomInstallCommand(install):
    def run(self):

        # windowsUrl = "http://10.0.0.64:4040/api/public/dl/gSh9w2TT/Peridyno/Release/PyPeridyno-windows/PyPeridyno-windows-1.2.1.zip"

        if sys.platform == 'win32':
            # windows
            print("Running Windows install")

            if copyData():
                print("copy data successfully")
            else:
                print("copy data failed")
                sys.exit(0)

            # HeightField
            # if copyCufft():
            #     print("copy cufft successfully")
            # else:
            #     print("copy cufft failed")
            #     sys.exit(0)

            # Qt
            # if checkQt():
            #     print("checkQt successfully")
            # else:
            #     print("Please install Qt")
            #     sys.exit(0)

            # if extractLocal(localZipPath):
            #     print("Local extraction complete!")
            # else:
            #     print("Local extraction failed!")
            #     sys.exit(0)

            # if downloadExtract(windowsUrl):
            #     print("Download complete")
            # else:
            #     print("Download failed")
            #     sys.exit(0)

            install.run(self)
        elif sys.platform.startswith('linux'):
            # linux
            print("Running Linux install")
            install.run(self)


setuptools.setup(
    #name="PyPeridyno",
    #name="PyPeridyno_DualParticleSystem",
    #name="PyPeridyno_HeightField",
    #name="PyPeridyno_Modeling",
    #name="PyPeridyno_Multiphysics",
    #name="PyPeridyno_ParticleSystem",
    #name="PyPeridyno_Peridynamics",
    #name="PyPeridyno_Qt",
    #name="PyPeridyno_RigidBody",
    #name="PyPeridyno_SemiAnalyticalScheme",
    #name="PyPeridyno_Topology",
    #name="PyPeridyno_Volume",
    
    version="1.2.1",
    author="unibeam",
    author_email="xiaowei@iscas.ac.cn",
    description="A python package for Peridyno",
    long_description=open('README.rst').read(),
    long_description_content_type="text/markdown",
    license='Apache License, Version 2.0',
    url="https://peridyno.com/",
    packages=find_packages(),
    # package_dir={'PyPeridyno':'src'}
    package_data={
        'PyPeridyno_SemiAnalyticalScheme': ['*.dll', '*.pyd', '*.lib', '*.exe'],
    },
    data_files=[
        ('.', [f for pattern in ['src/*.dll', 'src/*.pyd', 'src/*.lib',
         'src/*.exe', 'src/*.exp'] for f in glob.glob(pattern)])
    ],
    install_requires=[
        # PyPeridyno
        #"PyPeridyno_Topology==1.2.1"

        # PyPeridyno_DualParticleSystem
        # "PyPeridyno==1.2.1",
        # "PyPeridyno_SemiAnalyticalScheme==1.2.1",
        # "PyPeridyno_ParticleSystem==1.2.1",
        # "PyPeridyno_Modeling==1.2.1",
        # "PyPeridyno_Topology==1.2.1"

        # PyPeridyno_HeightField
        # "PyPeridyno==1.2.1",
        # "PyPeridyno_Topology==1.2.1",
        # "PyPeridyno_RigidBody==1.2.1",
        # "PyPeridyno_Modeling==1.2.1",

        # PyPeridyno_Modeling
        # "PyPeridyno==1.2.1",
        # "PyPeridyno_Topology==1.2.1",

        # PyPeridyno_Multiphysics
        # "PyPeridyno==1.2.1",
        # "PyPeridyno_Topology==1.2.1",
        # "PyPeridyno_Modeling==1.2.1",
        # "PyPeridyno_RigidBody==1.2.1",
        # "PyPeridyno_ParticleSystem==1.2.1",
        # "PyPeridyno_Volume==1.2.1",
        # "PyPeridyno_Peridynamics==1.2.1",

        # PyPeridyno_ParticleSystem
        # "PyPeridyno==1.2.1",
        # "PyPeridyno_Topology==1.2.1",
        # "PyPeridyno_Modeling==1.2.1",

        # PyPeridyno_Peridynamics
        # "PyPeridyno==1.2.1",
        # "PyPeridyno_Topology==1.2.1",
        # "PyPeridyno_Modeling==1.2.1",
        # "PyPeridyno_ParticleSystem==1.2.1",

        # PyPeridyno_Qt
        # "PyPeridyno==1.2.1",
        # "PyPeridyno_Topology==1.2.1",

        # PyPeridyno_RigidBody
        # "PyPeridyno==1.2.1",
        # "PyPeridyno_Topology==1.2.1",
        # "PyPeridyno_Modeling==1.2.1",

        # PyPeridyno_SemiAnalyticalScheme
        # "PyPeridyno==1.2.1",
        # "PyPeridyno_Topology==1.2.1",
        # "PyPeridyno_Modeling==1.2.1",
        # "PyPeridyno_ParticleSystem==1.2.1",

        # PyPeridyno_Topology

        # PyPeridyno_Volume
        # "PyPeridyno==1.2.1",
        # "PyPeridyno_Topology==1.2.1",
        # "PyPeridyno_Modeling==1.2.1",
        # 如果需要其他依赖，请列出
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
    python_requires='>=3.12',
)
