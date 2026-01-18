from setuptools import find_packages, setup
import os                  #追加。OSの機能のパッケージ
from glob import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')) #追加
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yasushi Ando',
    maintainer_email='yasushigit@hogehoge.com',
    description='a package for practice',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'encoder_talker = mypkg.encoder_talker:main', #encoder_talker.pyのmain関数という意味
            'encoder_listener = mypkg.encoder_listener:main', #lisner.pyのmain関数という意味
        ],
    },
)
