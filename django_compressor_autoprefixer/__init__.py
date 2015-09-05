from django.conf import settings
from compressor.filters import CompilerFilter


COMPRESS_AUTOPREFIXER_BINARY = "postcss"
COMPRESS_AUTOPREFIXER_ARGS = "--use autoprefixer"


class AutoprefixerFilter(CompilerFilter):
    command = "{binary} {args}"
    options = (
        ("binary", getattr(settings, "COMPRESS_AUTOPREFIXER_BINARY", COMPRESS_AUTOPREFIXER_BINARY)),
        ("args", getattr(settings, "COMPRESS_AUTOPREFIXER_ARGS", COMPRESS_AUTOPREFIXER_ARGS)),
    )
