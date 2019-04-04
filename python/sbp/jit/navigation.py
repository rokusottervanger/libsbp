#!/usr/bin/env python
# Copyright (C) 2015-2018 Swift Navigation Inc.
# Contact: Swift Navigation <dev@swiftnav.com>
#
# This source is subject to the license found in the file 'LICENSE' which must
# be be distributed together with this source. All other rights reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.


"""
Geodetic navigation messages reporting GPS time, position, velocity,
and baseline position solutions. For position solutions, these
messages define several different position solutions: single-point
(SPP), RTK, and pseudo-absolute position solutions.

The SPP is the standalone, absolute GPS position solution using only
a single receiver. The RTK solution is the differential GPS
solution, which can use either a fixed/integer or floating carrier
phase ambiguity. The pseudo-absolute position solution uses a
user-provided, well-surveyed base station position (if available)
and the RTK solution in tandem.

When the inertial navigation mode indicates that the IMU is used,
all messages are reported in the vehicle body frame as defined by
device settings.  By default, the vehicle body frame is configured to be
coincident with the antenna phase center.  When there is no inertial
navigation, the solution will be reported at the phase center of the antenna.
There is no inertial navigation capability on Piksi Multi or Duro. 

"""

import json

from sbp.jit.msg import SBP, SENDER_ID
from sbp.jit.msg import get_u8, get_u16, get_u32, get_u64
from sbp.jit.msg import get_s8, get_s16, get_s32, get_s64
from sbp.jit.msg import get_f32, get_f64
from sbp.jit.msg import get_string, get_fixed_string
from sbp.jit.msg import get_array, get_fixed_array

# Automatically generated from piksi/yaml/swiftnav/sbp/navigation.yaml with generate.py.
# Please do not hand edit!
SBP_MSG_GPS_TIME = 0x0102
class MsgGPSTime(SBP):
  """SBP class for message MSG_GPS_TIME (0x0102).

  You can have MSG_GPS_TIME inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the GPS time, representing the time since
the GPS epoch began on midnight January 6, 1980 UTC. GPS time
counts the weeks and seconds of the week. The weeks begin at the
Saturday/Sunday transition. GPS week 0 began at the beginning of
the GPS time scale.

Within each week number, the GPS time of the week is between
between 0 and 604800 seconds (=60*60*24*7). Note that GPS time
does not accumulate leap seconds, and as of now, has a small
offset from UTC. In a message stream, this message precedes a
set of other navigation messages referenced to the same time
(but lacking the ns field) and indicates a more precise time of
these messages.


  """
  __slots__ = ['wn',
               'tow',
               'ns_residual',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__wn, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__ns_residual, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'wn' : __wn,
      'tow' : __tow,
      'ns_residual' : __ns_residual,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.wn = res['wn']
    self.tow = res['tow']
    self.ns_residual = res['ns_residual']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_UTC_TIME = 0x0103
class MsgUtcTime(SBP):
  """SBP class for message MSG_UTC_TIME (0x0103).

  You can have MSG_UTC_TIME inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the Universal Coordinated Time (UTC).  Note the flags
which indicate the source of the UTC offset value and source of the time fix.


  """
  __slots__ = ['flags',
               'tow',
               'year',
               'month',
               'day',
               'hours',
               'minutes',
               'seconds',
               'ns',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__year, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__month, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__day, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__hours, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__minutes, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__seconds, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__ns, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'flags' : __flags,
      'tow' : __tow,
      'year' : __year,
      'month' : __month,
      'day' : __day,
      'hours' : __hours,
      'minutes' : __minutes,
      'seconds' : __seconds,
      'ns' : __ns,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.flags = res['flags']
    self.tow = res['tow']
    self.year = res['year']
    self.month = res['month']
    self.day = res['day']
    self.hours = res['hours']
    self.minutes = res['minutes']
    self.seconds = res['seconds']
    self.ns = res['ns']
    return res, off, length
  
SBP_MSG_DOPS = 0x0208
class MsgDops(SBP):
  """SBP class for message MSG_DOPS (0x0208).

  You can have MSG_DOPS inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This dilution of precision (DOP) message describes the effect of
navigation satellite geometry on positional measurement
precision.  The flags field indicated whether the DOP reported
corresponds to differential or SPP solution.


  """
  __slots__ = ['tow',
               'gdop',
               'pdop',
               'tdop',
               'hdop',
               'vdop',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__gdop, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__pdop, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__tdop, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__hdop, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__vdop, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'gdop' : __gdop,
      'pdop' : __pdop,
      'tdop' : __tdop,
      'hdop' : __hdop,
      'vdop' : __vdop,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.gdop = res['gdop']
    self.pdop = res['pdop']
    self.tdop = res['tdop']
    self.hdop = res['hdop']
    self.vdop = res['vdop']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_POS_ECEF = 0x0209
class MsgPosECEF(SBP):
  """SBP class for message MSG_POS_ECEF (0x0209).

  You can have MSG_POS_ECEF inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The position solution message reports absolute Earth Centered
Earth Fixed (ECEF) coordinates and the status (single point vs
pseudo-absolute RTK) of the position solution. If the rover
receiver knows the surveyed position of the base station and has
an RTK solution, this reports a pseudo-absolute position
solution using the base station position and the rover's RTK
baseline vector. The full GPS time is given by the preceding
MSG_GPS_TIME with the matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'x',
               'y',
               'z',
               'accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__x, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__y, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__z, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'x' : __x,
      'y' : __y,
      'z' : __z,
      'accuracy' : __accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.x = res['x']
    self.y = res['y']
    self.z = res['z']
    self.accuracy = res['accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_POS_ECEF_COV = 0x0214
class MsgPosECEFCov(SBP):
  """SBP class for message MSG_POS_ECEF_COV (0x0214).

  You can have MSG_POS_ECEF_COV inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The position solution message reports absolute Earth Centered
Earth Fixed (ECEF) coordinates and the status (single point vs
pseudo-absolute RTK) of the position solution. The message also
reports the upper triangular portion of the 3x3 covariance matrix.
If the receiver knows the surveyed position of the base station and has
an RTK solution, this reports a pseudo-absolute position
solution using the base station position and the rover's RTK
baseline vector. The full GPS time is given by the preceding
MSG_GPS_TIME with the matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'x',
               'y',
               'z',
               'cov_x_x',
               'cov_x_y',
               'cov_x_z',
               'cov_y_y',
               'cov_y_z',
               'cov_z_z',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__x, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__y, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__z, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_x_x, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_x_y, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_x_z, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_y_y, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_y_z, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_z_z, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'x' : __x,
      'y' : __y,
      'z' : __z,
      'cov_x_x' : __cov_x_x,
      'cov_x_y' : __cov_x_y,
      'cov_x_z' : __cov_x_z,
      'cov_y_y' : __cov_y_y,
      'cov_y_z' : __cov_y_z,
      'cov_z_z' : __cov_z_z,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.x = res['x']
    self.y = res['y']
    self.z = res['z']
    self.cov_x_x = res['cov_x_x']
    self.cov_x_y = res['cov_x_y']
    self.cov_x_z = res['cov_x_z']
    self.cov_y_y = res['cov_y_y']
    self.cov_y_z = res['cov_y_z']
    self.cov_z_z = res['cov_z_z']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_POS_LLH = 0x020A
class MsgPosLLH(SBP):
  """SBP class for message MSG_POS_LLH (0x020A).

  You can have MSG_POS_LLH inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This position solution message reports the absolute geodetic
coordinates and the status (single point vs pseudo-absolute RTK)
of the position solution. If the rover receiver knows the
surveyed position of the base station and has an RTK solution,
this reports a pseudo-absolute position solution using the base
station position and the rover's RTK baseline vector. The full
GPS time is given by the preceding MSG_GPS_TIME with the
matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'lat',
               'lon',
               'height',
               'h_accuracy',
               'v_accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__lat, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__lon, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__height, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__h_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__v_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'lat' : __lat,
      'lon' : __lon,
      'height' : __height,
      'h_accuracy' : __h_accuracy,
      'v_accuracy' : __v_accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.lat = res['lat']
    self.lon = res['lon']
    self.height = res['height']
    self.h_accuracy = res['h_accuracy']
    self.v_accuracy = res['v_accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_POS_LLH_COV = 0x0211
class MsgPosLLHCov(SBP):
  """SBP class for message MSG_POS_LLH_COV (0x0211).

  You can have MSG_POS_LLH_COV inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This position solution message reports the absolute geodetic
coordinates and the status (single point vs pseudo-absolute RTK)
of the position solution as well as the upper triangle of the 3x3
covariance matrix.  The position information and Fix Mode flags should
follow the MSG_POS_LLH message.  Since the covariance matrix is computed
in the local-level North, East, Down frame, the covariance terms follow
with that convention. Thus, covariances are reported against the "downward"
measurement and care should be taken with the sign convention.


  """
  __slots__ = ['tow',
               'lat',
               'lon',
               'height',
               'cov_n_n',
               'cov_n_e',
               'cov_n_d',
               'cov_e_e',
               'cov_e_d',
               'cov_d_d',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__lat, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__lon, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__height, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_n_n, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_n_e, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_n_d, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_e_e, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_e_d, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_d_d, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'lat' : __lat,
      'lon' : __lon,
      'height' : __height,
      'cov_n_n' : __cov_n_n,
      'cov_n_e' : __cov_n_e,
      'cov_n_d' : __cov_n_d,
      'cov_e_e' : __cov_e_e,
      'cov_e_d' : __cov_e_d,
      'cov_d_d' : __cov_d_d,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.lat = res['lat']
    self.lon = res['lon']
    self.height = res['height']
    self.cov_n_n = res['cov_n_n']
    self.cov_n_e = res['cov_n_e']
    self.cov_n_d = res['cov_n_d']
    self.cov_e_e = res['cov_e_e']
    self.cov_e_d = res['cov_e_d']
    self.cov_d_d = res['cov_d_d']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_BASELINE_ECEF = 0x020B
class MsgBaselineECEF(SBP):
  """SBP class for message MSG_BASELINE_ECEF (0x020B).

  You can have MSG_BASELINE_ECEF inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the baseline solution in Earth Centered
Earth Fixed (ECEF) coordinates. This baseline is the relative
vector distance from the base station to the rover receiver. The
full GPS time is given by the preceding MSG_GPS_TIME with the
matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'x',
               'y',
               'z',
               'accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__x, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__y, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__z, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'x' : __x,
      'y' : __y,
      'z' : __z,
      'accuracy' : __accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.x = res['x']
    self.y = res['y']
    self.z = res['z']
    self.accuracy = res['accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_BASELINE_NED = 0x020C
class MsgBaselineNED(SBP):
  """SBP class for message MSG_BASELINE_NED (0x020C).

  You can have MSG_BASELINE_NED inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the baseline solution in North East Down
(NED) coordinates. This baseline is the relative vector distance
from the base station to the rover receiver, and NED coordinate
system is defined at the local WGS84 tangent plane centered at the
base station position.  The full GPS time is given by the
preceding MSG_GPS_TIME with the matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'n',
               'e',
               'd',
               'h_accuracy',
               'v_accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__e, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__d, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__h_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__v_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'n' : __n,
      'e' : __e,
      'd' : __d,
      'h_accuracy' : __h_accuracy,
      'v_accuracy' : __v_accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.n = res['n']
    self.e = res['e']
    self.d = res['d']
    self.h_accuracy = res['h_accuracy']
    self.v_accuracy = res['v_accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_VEL_ECEF = 0x020D
class MsgVelECEF(SBP):
  """SBP class for message MSG_VEL_ECEF (0x020D).

  You can have MSG_VEL_ECEF inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the velocity in Earth Centered Earth Fixed
(ECEF) coordinates. The full GPS time is given by the preceding
MSG_GPS_TIME with the matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'x',
               'y',
               'z',
               'accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__x, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__y, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__z, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'x' : __x,
      'y' : __y,
      'z' : __z,
      'accuracy' : __accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.x = res['x']
    self.y = res['y']
    self.z = res['z']
    self.accuracy = res['accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_VEL_ECEF_COV = 0x0215
class MsgVelECEFCov(SBP):
  """SBP class for message MSG_VEL_ECEF_COV (0x0215).

  You can have MSG_VEL_ECEF_COV inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the velocity in Earth Centered Earth Fixed
(ECEF) coordinates. The full GPS time is given by the preceding
MSG_GPS_TIME with the matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'x',
               'y',
               'z',
               'cov_x_x',
               'cov_x_y',
               'cov_x_z',
               'cov_y_y',
               'cov_y_z',
               'cov_z_z',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__x, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__y, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__z, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_x_x, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_x_y, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_x_z, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_y_y, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_y_z, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_z_z, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'x' : __x,
      'y' : __y,
      'z' : __z,
      'cov_x_x' : __cov_x_x,
      'cov_x_y' : __cov_x_y,
      'cov_x_z' : __cov_x_z,
      'cov_y_y' : __cov_y_y,
      'cov_y_z' : __cov_y_z,
      'cov_z_z' : __cov_z_z,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.x = res['x']
    self.y = res['y']
    self.z = res['z']
    self.cov_x_x = res['cov_x_x']
    self.cov_x_y = res['cov_x_y']
    self.cov_x_z = res['cov_x_z']
    self.cov_y_y = res['cov_y_y']
    self.cov_y_z = res['cov_y_z']
    self.cov_z_z = res['cov_z_z']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_VEL_NED = 0x020E
class MsgVelNED(SBP):
  """SBP class for message MSG_VEL_NED (0x020E).

  You can have MSG_VEL_NED inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the velocity in local North East Down (NED)
coordinates. The NED coordinate system is defined as the local WGS84
tangent plane centered at the current position. The full GPS time is
given by the preceding MSG_GPS_TIME with the matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'n',
               'e',
               'd',
               'h_accuracy',
               'v_accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__e, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__d, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__h_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__v_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'n' : __n,
      'e' : __e,
      'd' : __d,
      'h_accuracy' : __h_accuracy,
      'v_accuracy' : __v_accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.n = res['n']
    self.e = res['e']
    self.d = res['d']
    self.h_accuracy = res['h_accuracy']
    self.v_accuracy = res['v_accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_VEL_NED_COV = 0x0212
class MsgVelNEDCov(SBP):
  """SBP class for message MSG_VEL_NED_COV (0x0212).

  You can have MSG_VEL_NED_COV inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the velocity in local North East Down (NED)
coordinates. The NED coordinate system is defined as the local WGS84
tangent plane centered at the current position. The full GPS time is
given by the preceding MSG_GPS_TIME with the matching time-of-week (tow).
This message is similar to the MSG_VEL_NED, but it includes the upper triangular
portion of the 3x3 covariance matrix.


  """
  __slots__ = ['tow',
               'n',
               'e',
               'd',
               'cov_n_n',
               'cov_n_e',
               'cov_n_d',
               'cov_e_e',
               'cov_e_d',
               'cov_d_d',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__e, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__d, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_n_n, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_n_e, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_n_d, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_e_e, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_e_d, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_d_d, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'n' : __n,
      'e' : __e,
      'd' : __d,
      'cov_n_n' : __cov_n_n,
      'cov_n_e' : __cov_n_e,
      'cov_n_d' : __cov_n_d,
      'cov_e_e' : __cov_e_e,
      'cov_e_d' : __cov_e_d,
      'cov_d_d' : __cov_d_d,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.n = res['n']
    self.e = res['e']
    self.d = res['d']
    self.cov_n_n = res['cov_n_n']
    self.cov_n_e = res['cov_n_e']
    self.cov_n_d = res['cov_n_d']
    self.cov_e_e = res['cov_e_e']
    self.cov_e_d = res['cov_e_d']
    self.cov_d_d = res['cov_d_d']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_VEL_BODY = 0x0213
class MsgVelBody(SBP):
  """SBP class for message MSG_VEL_BODY (0x0213).

  You can have MSG_VEL_BODY inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the velocity in the Vehicle Body Frame. By convention,
the x-axis should point out the nose of the vehicle and represent the forward
direction, while as the y-axis should point out the right hand side of the vehicle.
Since this is a right handed system, z should point out the bottom of the vehicle.
The orientation and origin of the Vehicle Body Frame are specified via the device settings.
The full GPS time is given by the preceding MSG_GPS_TIME with the
matching time-of-week (tow). This message is only produced by inertial versions of Swift
products and is not available from Piksi Multi or Duro.


  """
  __slots__ = ['tow',
               'x',
               'y',
               'z',
               'cov_x_x',
               'cov_x_y',
               'cov_x_z',
               'cov_y_y',
               'cov_y_z',
               'cov_z_z',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__x, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__y, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__z, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_x_x, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_x_y, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_x_z, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_y_y, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_y_z, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__cov_z_z, offset, length) = offset, get_f32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'x' : __x,
      'y' : __y,
      'z' : __z,
      'cov_x_x' : __cov_x_x,
      'cov_x_y' : __cov_x_y,
      'cov_x_z' : __cov_x_z,
      'cov_y_y' : __cov_y_y,
      'cov_y_z' : __cov_y_z,
      'cov_z_z' : __cov_z_z,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.x = res['x']
    self.y = res['y']
    self.z = res['z']
    self.cov_x_x = res['cov_x_x']
    self.cov_x_y = res['cov_x_y']
    self.cov_x_z = res['cov_x_z']
    self.cov_y_y = res['cov_y_y']
    self.cov_y_z = res['cov_y_z']
    self.cov_z_z = res['cov_z_z']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_AGE_CORRECTIONS = 0x0210
class MsgAgeCorrections(SBP):
  """SBP class for message MSG_AGE_CORRECTIONS (0x0210).

  You can have MSG_AGE_CORRECTIONS inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the Age of the corrections used for the current
Differential solution


  """
  __slots__ = ['tow',
               'age',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__age, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'age' : __age,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.age = res['age']
    return res, off, length
  
SBP_MSG_GPS_TIME_DEP_A = 0x0100
class MsgGPSTimeDepA(SBP):
  """SBP class for message MSG_GPS_TIME_DEP_A (0x0100).

  You can have MSG_GPS_TIME_DEP_A inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the GPS time, representing the time since
the GPS epoch began on midnight January 6, 1980 UTC. GPS time
counts the weeks and seconds of the week. The weeks begin at the
Saturday/Sunday transition. GPS week 0 began at the beginning of
the GPS time scale.

Within each week number, the GPS time of the week is between
between 0 and 604800 seconds (=60*60*24*7). Note that GPS time
does not accumulate leap seconds, and as of now, has a small
offset from UTC. In a message stream, this message precedes a
set of other navigation messages referenced to the same time
(but lacking the ns field) and indicates a more precise time of
these messages.


  """
  __slots__ = ['wn',
               'tow',
               'ns_residual',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__wn, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__ns_residual, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'wn' : __wn,
      'tow' : __tow,
      'ns_residual' : __ns_residual,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.wn = res['wn']
    self.tow = res['tow']
    self.ns_residual = res['ns_residual']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_DOPS_DEP_A = 0x0206
class MsgDopsDepA(SBP):
  """SBP class for message MSG_DOPS_DEP_A (0x0206).

  You can have MSG_DOPS_DEP_A inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This dilution of precision (DOP) message describes the effect of
navigation satellite geometry on positional measurement
precision.


  """
  __slots__ = ['tow',
               'gdop',
               'pdop',
               'tdop',
               'hdop',
               'vdop',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__gdop, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__pdop, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__tdop, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__hdop, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__vdop, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'gdop' : __gdop,
      'pdop' : __pdop,
      'tdop' : __tdop,
      'hdop' : __hdop,
      'vdop' : __vdop,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.gdop = res['gdop']
    self.pdop = res['pdop']
    self.tdop = res['tdop']
    self.hdop = res['hdop']
    self.vdop = res['vdop']
    return res, off, length
  
SBP_MSG_POS_ECEF_DEP_A = 0x0200
class MsgPosECEFDepA(SBP):
  """SBP class for message MSG_POS_ECEF_DEP_A (0x0200).

  You can have MSG_POS_ECEF_DEP_A inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The position solution message reports absolute Earth Centered
Earth Fixed (ECEF) coordinates and the status (single point vs
pseudo-absolute RTK) of the position solution. If the rover
receiver knows the surveyed position of the base station and has
an RTK solution, this reports a pseudo-absolute position
solution using the base station position and the rover's RTK
baseline vector. The full GPS time is given by the preceding
MSG_GPS_TIME with the matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'x',
               'y',
               'z',
               'accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__x, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__y, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__z, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'x' : __x,
      'y' : __y,
      'z' : __z,
      'accuracy' : __accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.x = res['x']
    self.y = res['y']
    self.z = res['z']
    self.accuracy = res['accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_POS_LLH_DEP_A = 0x0201
class MsgPosLLHDepA(SBP):
  """SBP class for message MSG_POS_LLH_DEP_A (0x0201).

  You can have MSG_POS_LLH_DEP_A inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This position solution message reports the absolute geodetic
coordinates and the status (single point vs pseudo-absolute RTK)
of the position solution. If the rover receiver knows the
surveyed position of the base station and has an RTK solution,
this reports a pseudo-absolute position solution using the base
station position and the rover's RTK baseline vector. The full
GPS time is given by the preceding MSG_GPS_TIME with the
matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'lat',
               'lon',
               'height',
               'h_accuracy',
               'v_accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__lat, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__lon, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__height, offset, length) = offset, get_f64(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__h_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__v_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'lat' : __lat,
      'lon' : __lon,
      'height' : __height,
      'h_accuracy' : __h_accuracy,
      'v_accuracy' : __v_accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.lat = res['lat']
    self.lon = res['lon']
    self.height = res['height']
    self.h_accuracy = res['h_accuracy']
    self.v_accuracy = res['v_accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_BASELINE_ECEF_DEP_A = 0x0202
class MsgBaselineECEFDepA(SBP):
  """SBP class for message MSG_BASELINE_ECEF_DEP_A (0x0202).

  You can have MSG_BASELINE_ECEF_DEP_A inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the baseline solution in Earth Centered
Earth Fixed (ECEF) coordinates. This baseline is the relative
vector distance from the base station to the rover receiver. The
full GPS time is given by the preceding MSG_GPS_TIME with the
matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'x',
               'y',
               'z',
               'accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__x, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__y, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__z, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'x' : __x,
      'y' : __y,
      'z' : __z,
      'accuracy' : __accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.x = res['x']
    self.y = res['y']
    self.z = res['z']
    self.accuracy = res['accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_BASELINE_NED_DEP_A = 0x0203
class MsgBaselineNEDDepA(SBP):
  """SBP class for message MSG_BASELINE_NED_DEP_A (0x0203).

  You can have MSG_BASELINE_NED_DEP_A inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the baseline solution in North East Down
(NED) coordinates. This baseline is the relative vector distance
from the base station to the rover receiver, and NED coordinate
system is defined at the local WGS84 tangent plane centered at the
base station position.  The full GPS time is given by the
preceding MSG_GPS_TIME with the matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'n',
               'e',
               'd',
               'h_accuracy',
               'v_accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__e, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__d, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__h_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__v_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'n' : __n,
      'e' : __e,
      'd' : __d,
      'h_accuracy' : __h_accuracy,
      'v_accuracy' : __v_accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.n = res['n']
    self.e = res['e']
    self.d = res['d']
    self.h_accuracy = res['h_accuracy']
    self.v_accuracy = res['v_accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_VEL_ECEF_DEP_A = 0x0204
class MsgVelECEFDepA(SBP):
  """SBP class for message MSG_VEL_ECEF_DEP_A (0x0204).

  You can have MSG_VEL_ECEF_DEP_A inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the velocity in Earth Centered Earth Fixed
(ECEF) coordinates. The full GPS time is given by the preceding
MSG_GPS_TIME with the matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'x',
               'y',
               'z',
               'accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__x, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__y, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__z, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'x' : __x,
      'y' : __y,
      'z' : __z,
      'accuracy' : __accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.x = res['x']
    self.y = res['y']
    self.z = res['z']
    self.accuracy = res['accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_VEL_NED_DEP_A = 0x0205
class MsgVelNEDDepA(SBP):
  """SBP class for message MSG_VEL_NED_DEP_A (0x0205).

  You can have MSG_VEL_NED_DEP_A inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the velocity in local North East Down (NED)
coordinates. The NED coordinate system is defined as the local WGS84
tangent plane centered at the current position. The full GPS time is
given by the preceding MSG_GPS_TIME with the matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'n',
               'e',
               'd',
               'h_accuracy',
               'v_accuracy',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__e, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__d, offset, length) = offset, get_s32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__h_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__v_accuracy, offset, length) = offset, get_u16(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'n' : __n,
      'e' : __e,
      'd' : __d,
      'h_accuracy' : __h_accuracy,
      'v_accuracy' : __v_accuracy,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.n = res['n']
    self.e = res['e']
    self.d = res['d']
    self.h_accuracy = res['h_accuracy']
    self.v_accuracy = res['v_accuracy']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  
SBP_MSG_BASELINE_HEADING_DEP_A = 0x0207
class MsgBaselineHeadingDepA(SBP):
  """SBP class for message MSG_BASELINE_HEADING_DEP_A (0x0207).

  You can have MSG_BASELINE_HEADING_DEP_A inherit its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  This message reports the baseline heading pointing from the base station
to the rover relative to True North. The full GPS time is given by the
preceding MSG_GPS_TIME with the matching time-of-week (tow).


  """
  __slots__ = ['tow',
               'heading',
               'n_sats',
               'flags',
               ]
  @classmethod
  def parse_members(cls, buf, offset, length):
    o_0 = offset
    o_1, (__tow, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__heading, offset, length) = offset, get_u32(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__n_sats, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    o_1, (__flags, offset, length) = offset, get_u8(buf, offset, length)
    if o_1 == offset:
      return {}, o_0, length
    return {
      'tow' : __tow,
      'heading' : __heading,
      'n_sats' : __n_sats,
      'flags' : __flags,
    }, offset, length

  def _unpack_members(self, buf, offset, length):
    res, off, length = self.parse_members(buf, offset, length)
    if off == offset:
      return {}, offset, length
    self.tow = res['tow']
    self.heading = res['heading']
    self.n_sats = res['n_sats']
    self.flags = res['flags']
    return res, off, length
  

msg_classes = {
  0x0102: MsgGPSTime,
  0x0103: MsgUtcTime,
  0x0208: MsgDops,
  0x0209: MsgPosECEF,
  0x0214: MsgPosECEFCov,
  0x020A: MsgPosLLH,
  0x0211: MsgPosLLHCov,
  0x020B: MsgBaselineECEF,
  0x020C: MsgBaselineNED,
  0x020D: MsgVelECEF,
  0x0215: MsgVelECEFCov,
  0x020E: MsgVelNED,
  0x0212: MsgVelNEDCov,
  0x0213: MsgVelBody,
  0x0210: MsgAgeCorrections,
  0x0100: MsgGPSTimeDepA,
  0x0206: MsgDopsDepA,
  0x0200: MsgPosECEFDepA,
  0x0201: MsgPosLLHDepA,
  0x0202: MsgBaselineECEFDepA,
  0x0203: MsgBaselineNEDDepA,
  0x0204: MsgVelECEFDepA,
  0x0205: MsgVelNEDDepA,
  0x0207: MsgBaselineHeadingDepA,
}