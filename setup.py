from distutils.core import setup

setup(name="calc",
      entry_points={
          'console_scripts': [
              'calc = calc:main', ]},
      version="0.0.2",
      description="A Simple Tkinter Calc",
      author="Oles Pisarenko",
      author_email="doctor.mailbox@mail.ru",
      url="http://www.ya.ru",
      packages=["calc"]
      )
