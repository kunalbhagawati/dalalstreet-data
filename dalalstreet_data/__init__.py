try:
    from importlib import metadata
except ImportError:
    # Python < 3.8
    import importlib_metadata as metadata # type: ignore

try:
    __version__ = metadata.version("dalalstreet-data")
except metadata.PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

