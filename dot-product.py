import pynq
import numpy as np

# program the device
ol = pynq.Overlay("/work/shared/users/phd/atb78/pynq-ex/build/kernel.xclbin")
kernel = ol.kernel_1

# allocate buffers
a0 = pynq.allocate((8,), np.uint32)
b0 = pynq.allocate((8,), np.uint32)
v = pynq.allocate((1,), np.uint32)

# initialize input
a0[:] = np.random.randint(low=0, high=100, size=(8,), dtype=np.uint32)
b0[:] = np.random.randint(low=0, high=100, size=(8,), dtype=np.uint32)

# send data to the device
a0.sync_to_device()
b0.sync_to_device()

print("after sync")
# call kernel
kernel.call(a0, b0, v)
print("after execution")

# get data from the device
v.sync_from_device()

# check results
print(v)
# msg = "SUCCESS!" if np.array_equal(out, in1_vadd + in2_vadd) else "FAILURE!"
# print(msg)

# clean up
del a0
del b0
del v
ol.free()
pynq.Device.active_device.close()
