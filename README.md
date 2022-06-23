# PYNQ RTL Kernel Example

## Requirements

Install PYNQ with pip or conda.

## How to use
Change `DEVICE` variable in Makefile. Source vitis/vivado setup.

In root directory:
```
emconfigutil --platform <platform_name>
export XCL_EMULATION_MODE=hw_emu
export EMCONFIG_PATH=`pwd`
make
```

Change xclbin location in `dot-product.py`.

```
python dot-product.py
```
