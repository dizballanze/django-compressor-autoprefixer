from django.conf import settings
from compressor.filters import CompilerFilter


COMPRESS_AUTOPREFIXER_BINARY = "autoprefixer"
COMPRESS_AUTOPREFIXER_ARGS = ""


class AutoprefixerFilter(CompilerFilter):
    command = "{binary} {args}"
    options = (
        ("binary", settings.COMPRESS_AUTOPREFIXER_BINARY or COMPRESS_AUTOPREFIXER_BINARY),
        ("args", settings.COMPRESS_AUTOPREFIXER_ARGS or COMPRESS_AUTOPREFIXER_ARGS),
    )
