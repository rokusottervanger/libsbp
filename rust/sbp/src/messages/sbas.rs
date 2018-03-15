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
// Automatically generated from yaml/swiftnav/sbp/sbas.yaml
// with generate.py. Please do not hand edit!
//****************************************************************************/

// SBAS data
extern crate byteorder;
#[allow(unused_imports)]
use self::byteorder::{LittleEndian,ReadBytesExt};
use super::gnss::*;


// Raw SBAS data
//
// This message is sent once per second per SBAS satellite. ME checks the
// parity of the data block and sends only blocks that pass the check.
//
#[derive(Debug)]
#[allow(non_snake_case)]
pub struct MsgSbasRaw {
    pub sid: GnssSignal,
        // ^ GNSS signal identifier.
    pub tow: u32,
        // ^ GPS time-of-week at the start of the data block.
    pub message_type: u8,
        // ^ SBAS message type (0-63)
    pub data: Vec<u8>,
        // ^ Raw SBAS data field of 212 bits (last byte padded with zeros).
}

impl MsgSbasRaw {
    pub const TYPE: u16 = 30583;
    pub fn parse(_buf: &mut &[u8]) -> Result<MsgSbasRaw, ::Error> {
        Ok( MsgSbasRaw{
            sid: GnssSignal::parse(_buf)?,
            tow: _buf.read_u32::<LittleEndian>()?,
            message_type: _buf.read_u8()?,
            data: ::read_u8_array_limit(_buf, 27)?,
        } )
    }
}

