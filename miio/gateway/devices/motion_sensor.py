"""Xiaomi Zigbee motion."""

from .subdevice import SubDevice


class MotionDevice(SubDevice):
    """Base class for subdevice motion."""

    properties = []


class Motion(MotionDevice):
    """Subdevice Motion specific properties and methods."""

    properties = []
    _zigbee_model = "lumi.sensor_motion.v2"
    _model = "RTCGQ01LM"
    _name = "Motion sensor"


class AqaraMotion(MotionDevice):
    """Subdevice AqaraMotion specific properties and methods."""

    properties = []
    _zigbee_model = "lumi.sensor_motion.aq2"
    _model = "RTCGQ11LM"
    _name = "Motion sensor"
