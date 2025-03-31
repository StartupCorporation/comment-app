from pathlib import Path

from dw_python_clis import ConfigVar, inner


namespace = inner

namespace.configure(
    options={
        ConfigVar.ROOT_DIR: Path(__file__).parent.parent,
    },
)
