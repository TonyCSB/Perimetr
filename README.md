# Perimetr

A dead hand system that monitor changes in network device and act accordingly.

## Installation

```bash
python3 -m pip install Perimetr
```

## Usage

```python
from Perimetr import Monitor

monitor = Monitor("IP", "192.168.0.1", 15, print, "Target is offline")
monitor.activate()
>> Target is offline
```

## Documentation

```python
def __init__(self, method, target, interval, callback, *args, retry=0,
        offline=True, all=True, delay=None, **kwargs):
        """Init the monitor with appropriate parameters. Currently support
        monitor device status with IP address and MAC address. Require the
        target device to be within same network.

        Parameters
        ----------
        method : str
            Takes "IP" or "MAC" as values. Used to specifies the ways to probe
            target devices. Must match the type of `target` parameter. Currently
            only check by IP address is supported.

        target : str || [str]
            The IP or MAC address of the target device(s). Must match the type
            of `method` parameter. If multiple target passed in, then all of
            them will be checked.

        interval : int
            The number of seconds until next check.

        callback : callable
            The callback function when device status change meets the required
            criteria. Will be called with `args` and `kwargs`.

        retry : int, optional
            Number of times to retry with `interval` apart until the system
            is considered triggered. Default is no retry.

        offline : bool, optional
            Triggers the callback function when device went offline or online.
            Default to when device went offline.

        all : bool, optional
            Used when multiple targets are passed in. If true, then all targets
            need to meet criteria before system triggered. Else, only one device
            status is required. Default to True.

        delay : int, optional
            The number of seconds delay of execute callback after triggered.
            Default is None.

        *args : arguments
            Used for callback function.

        **kwargs : keyword arguments
            Used for callback function.

        Raises
        ------
        ValueError
            When method provided is incorrect, or target provided mismatch
            with the method.
        """
```