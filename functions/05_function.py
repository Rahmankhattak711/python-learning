import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from functions.user_auth import main

print(main())
