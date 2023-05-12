from setuptools import setup

package_name = 'BurguerPack'
entry_point = 'Burguer'
function_name = 'main'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='igorunix',
    maintainer_email='igorunix@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            entry_point + ' = ' + package_name + ':' + function_name,
        ],
    },
)
