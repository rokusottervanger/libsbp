// Copyright (C) 2015-2018 Swift Navigation Inc.
// Contact: Swift Navigation <dev@swiftnav.com>
//
// This source is subject to the license found in the file 'LICENSE' which must
// be be distributed together with this source. All other rights reserved.
//
// THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
// EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
// WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.

//****************************************************************************
// Automatically generated from yaml/swiftnav/sbp/ndb.yaml
// with generate.py. Please do not hand edit!
//****************************************************************************/

// Messages for logging NDB events.
extern crate byteorder;
#[allow(unused_imports)]
use self::byteorder::{LittleEndian,ReadBytesExt};
use super::gnss::*;


// Navigation DataBase Event
//
// This message is sent out when an object is stored into NDB. If needed
// message could also be sent out when fetching an object from NDB.
//
#[derive(Debug)]
#[allow(non_snake_case)]
pub struct MsgNdbEvent {
    pub recv_time: u64,
        // ^ HW time in milliseconds.
    pub event: u8,
        // ^ Event type.
    pub object_type: u8,
        // ^ Event object type.
    pub result: u8,
        // ^ Event result.
    pub data_source: u8,
        // ^ Data source for STORE event, reserved for other events.
    pub object_sid: GnssSignal,
        // ^ GNSS signal identifier, If object_type is Ephemeris OR Almanac, sid
        // indicates for which signal the object belongs to. Reserved in other
        // cases.
    pub src_sid: GnssSignal,
        // ^ GNSS signal identifier, If object_type is Almanac, Almanac WN, Iono OR
        // L2C capabilities AND data_source is NDB_DS_RECEIVER sid indicates from
        // which SV data was decoded. Reserved in other cases.
    pub original_sender: u16,
        // ^ A unique identifier of the sending hardware. For v1.0, set to the 2
        // least significant bytes of the device serial number, valid only if
        // data_source is NDB_DS_SBP. Reserved in case of other data_source.
}

impl MsgNdbEvent {
    pub const TYPE: u16 = 1024;
    pub fn parse(_buf: &mut &[u8]) -> Result<MsgNdbEvent, ::Error> {
        Ok( MsgNdbEvent{
            recv_time: _buf.read_u64::<LittleEndian>()?,
            event: _buf.read_u8()?,
            object_type: _buf.read_u8()?,
            result: _buf.read_u8()?,
            data_source: _buf.read_u8()?,
            object_sid: GnssSignal::parse(_buf)?,
            src_sid: GnssSignal::parse(_buf)?,
            original_sender: _buf.read_u16::<LittleEndian>()?,
        } )
    }
}

