from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='rpi_utils',
      version='1.0',
      description='A Python module for various raspberry pi project utilities.',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python :: 3',
          'Operating System :: POSIX :: Linux',
      ],
    #   keywords='stepper motor mpu6050 raspberry',
    #   url='https://github.com/Tijndagamer/mpu6050',
      author='Cwilde921',
      author_email='wilde.utah@gmail.com',
      license='MIT',
      packages=['rpi_utils'],
    #   scripts=['bin/mpu6050-example'],
      zip_safe=False,
    #   long_description=readme()
    )
