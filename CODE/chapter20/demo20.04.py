from flake8.api import legacy as flake8
style_guide = flake8.get_style_guide(ignore=['F401', 'W503'])
style_guide.check_files(['test1.py'])
