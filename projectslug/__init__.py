from . import logger

try:
    import nuke
    import nukescripts
except ImportError:
    from projectslug.mock import nuke
else:
    from . import main
