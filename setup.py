from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine-tuning.
build_options = {
    'packages': [

    ],
    'excludes': [

    ],
    'zip_includes': [
        "ui/"
    ],
    'no_compress': True
}

base = 'gui'

executables = [
    Executable('HDZero_programmer_2.py', base=base, icon="")
]

setup(name='HDZero Programmer v2',
      version='0.1',
      description='Programmer for HDZero',
      options={'build_exe': build_options},
      executables=executables)
