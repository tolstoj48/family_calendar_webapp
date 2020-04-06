from .common import *
from .secret_key import *

if os.environ['kalendar'] == "prod":
    from .prod import *
else:
    from .local import *