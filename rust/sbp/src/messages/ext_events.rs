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
// Automatically generated from yaml/swiftnav/sbp/ext_events.yaml
// with generate.py. Please do not hand edit!
//****************************************************************************/

// Messages reporting accurately-timestamped external events,
// e.g. camera shutter time.
extern crate byteorder;
#[allow(unused_imports)]
use self::byteorder::{LittleEndian,ReadBytesExt};


// Reports timestamped external pin event
//
// Reports detection of an external event, the GPS time it occurred,
// which pin it was and whether it was rising or falling.
//
#[derive(Debug)]
#[allow(non_snake_case)]
pub struct MsgExtEvent {
    pub wn: u16,
        // ^ GPS week number
    pub tow: u32,
        // ^ GPS time of week rounded to the nearest millisecond
    pub ns_residual: i32,
        // ^ Nanosecond residual of millisecond-rounded TOW (ranges from -500000 to
        // 500000)
    pub flags: u8,
        // ^ Flags
    pub pin: u8,
        // ^ Pin number.  0..9 = DEBUG0..9.
}

impl MsgExtEvent {
    pub const TYPE: u16 = 257;
    pub fn parse(_buf: &mut &[u8]) -> Result<MsgExtEvent, ::Error> {
        Ok( MsgExtEvent{
            wn: _buf.read_u16::<LittleEndian>()?,
            tow: _buf.read_u32::<LittleEndian>()?,
            ns_residual: _buf.read_i32::<LittleEndian>()?,
            flags: _buf.read_u8()?,
            pin: _buf.read_u8()?,
        } )
    }
}

