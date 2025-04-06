use rand::Rng;
use byteorder::{ByteOrder, BigEndian};

#[repr(C)]
struct TCPHeader {
    source_port: u16,            // Source Port (16 bits)
    destination_port: u16,       // Destination Port (16 bits)
    sequence_number: u32,        // Sequence Number (32 bits)
    acknowledgement_number: u32, // Acknowledgment Number (32 bits)
    data_offset: u8,             // Data Offset (4 bits) + Reserved (3 bits) + Flags (9 bits)
    window_size: u16,            // Window Size (16 bits)
    checksum: u16,               // Checksum (16 bits)
    urgent_pointer: u16,         // Urgent Pointer (16 bits)
}

#[repr(C)]
struct IPHeader {
    version: u8,                 // Version (4 bits) + IHL (4 bits)
    type_of_service: u8,         // Type of Service (8 bits)
    total_length: u16,           // Total Length (16 bits)
    identification: u16,         // Identification (16 bits)
    flags: u8,                   // Flags (3 bits) + Fragment Offset (13 bits)
    fragment_offset: u16,        // Fragment Offset (13 bits)
    ttl: u8,                     // Time to Live (8 bits)
    protocol: u8,                // Protocol (8 bits)
    header_checksum: u16,        // Header Checksum (16 bits)
    source_address: u32,         // Source Address (32 bits)
    destination_address: u32,    // Destination Address (32 bits)
}

fn random_tcp_header() -> TCPHeader {
    let mut rng = rand::thread_rng();
    TCPHeader {
        source_port: rng.gen_range(1024..65535),
        destination_port: rng.gen_range(1024..65535),
        sequence_number: rng.gen(),
        acknowledgement_number: rng.gen(),
        data_offset: 5 << 4, // result: 80 in binary
        window_size: rng.gen_range(0..65535),
        checksum: 0, // Placeholder
        urgent_pointer: 0, // Placeholder
    }
}

fn random_ip_header() -> IPHeader {
    let mut rng = rand::thread_rng();
    IPHeader {
        version: 0x45, // Ipv4 and IHL of 5
        type_of_service: 0,
        total_length: 20 + 20,
        identification: rng.gen(),
        flags: 0,
        fragment_offset: 0,
        ttl: 64, // Common Default TTL
        protocol: 6, // TCP
        header_checksum: 0, // Placeholder
        source_address: rng.gen(),
        destination_address: rng.gen(),
    }
}

fn main() {
    // Generates random TCP and IP headers
    let tcp_header = random_tcp_header();
    let ip_header = random_ip_header();

    // Serializes the TCP header to a byte array
    let mut tcp_bytes = [0u8; std::mem::size_of::<TCPHeader>()];
    BigEndian::write_u16(&mut tcp_bytes[0..2], tcp_header.source_port);
    BigEndian::write_u16(&mut tcp_bytes[2..4], tcp_header.destination_port);
    BigEndian::write_u32(&mut tcp_bytes[4..8], tcp_header.sequence_number);
    BigEndian::write_u32(&mut tcp_bytes[8..12], tcp_header.acknowledgement_number);
    tcp_bytes[12] = tcp_header.data_offset;
    BigEndian::write_u16(&mut tcp_bytes[13..15], tcp_header.window_size);
    BigEndian::write_u16(&mut tcp_bytes[15..17], tcp_header.checksum);
    BigEndian::write_u16(&mut tcp_bytes[17..19], tcp_header.urgent_pointer);

    // Serializes the IP header to a byte array
    let mut ip_bytes = [0u8; std::mem::size_of::<IPHeader>()];
    ip_bytes[0] = ip_header.version;
    ip_bytes[1] = ip_header.type_of_service;
    BigEndian::write_u16(&mut ip_bytes[2..4], ip_header.total_length);
    BigEndian::write_u16(&mut ip_bytes[4..6], ip_header.identification);
    BigEndian::write_u16(&mut ip_bytes[6..8], ip_header.fragment_offset);
    ip_bytes[8] = ip_header.ttl;
    ip_bytes[9] = ip_header.protocol;
    BigEndian::write_u16(&mut ip_bytes[10..12], ip_header.header_checksum);
    BigEndian::write_u32(&mut ip_bytes[12..16], ip_header.source_address);
    BigEndian::write_u32(&mut ip_bytes[16..20], ip_header.destination_address);

    // Prints the serialized TCP and IP headers in bytes
    println!("TCP Header Bytes: {:?}", tcp_bytes);
    println!("IP Header Bytes: {:?}", ip_bytes);
}