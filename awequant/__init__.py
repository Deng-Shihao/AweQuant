"""Canonical import path for AweQuant with backward compatibility."""

from __future__ import annotations

import importlib


_gptqmodel = importlib.import_module("gptqmodel")

AweQuant = _gptqmodel.AweQuant
GPTQModel = _gptqmodel.GPTQModel
BaseQuantizeConfig = _gptqmodel.BaseQuantizeConfig
QuantizeConfig = _gptqmodel.QuantizeConfig
BACKEND = _gptqmodel.BACKEND
DEBUG_ON = _gptqmodel.DEBUG_ON
DEVICE_THREAD_POOL = _gptqmodel.DEVICE_THREAD_POOL
exllama_set_max_input_length = _gptqmodel.exllama_set_max_input_length
get_best_device = _gptqmodel.get_best_device
ASCII_LOGO = _gptqmodel.ASCII_LOGO
__version__ = _gptqmodel.__version__

# Reuse legacy package path so submodule imports like `awequant.quantization` resolve.
__path__ = _gptqmodel.__path__

__all__ = [
    "AweQuant",
    "GPTQModel",
    "BaseQuantizeConfig",
    "QuantizeConfig",
    "BACKEND",
    "DEBUG_ON",
    "DEVICE_THREAD_POOL",
    "exllama_set_max_input_length",
    "get_best_device",
    "ASCII_LOGO",
    "__version__",
]
