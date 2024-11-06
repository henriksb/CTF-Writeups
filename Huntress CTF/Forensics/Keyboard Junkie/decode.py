# USB HID key mapping based on common usage tables for standard keyboards
usb_hid_keycodes = {
    0x04: 'a', 0x05: 'b', 0x06: 'c', 0x07: 'd',
    0x08: 'e', 0x09: 'f', 0x0A: 'g', 0x0B: 'h',
    0x0C: 'i', 0x0D: 'j', 0x0E: 'k', 0x0F: 'l',
    0x10: 'm', 0x11: 'n', 0x12: 'o', 0x13: 'p',
    0x14: 'q', 0x15: 'r', 0x16: 's', 0x17: 't',
    0x18: 'u', 0x19: 'v', 0x1A: 'w', 0x1B: 'x',
    0x1C: 'y', 0x1D: 'z', 0x1E: '1', 0x1F: '2',
    0x20: '3', 0x21: '4', 0x22: '5', 0x23: '6',
    0x24: '7', 0x25: '8', 0x26: '9', 0x27: '0',
    0x28: 'Enter', 0x29: 'Esc', 0x2A: 'Backspace', 0x2B: 'Tab',
    0x2C: 'Space', 0x2D: '-', 0x2E: '=', 0x2F: '[',
    0x30: ']', 0x31: '\\', 0x33: ';', 0x34: "'",
    0x36: ',', 0x37: '.', 0x38: '/'
}

# Modifier key mapping (first byte)
usb_hid_modifiers = {
    0x01: 'Left Ctrl', 0x02: 'Left Shift', 0x04: 'Left Alt', 0x08: 'Left GUI',
    0x10: 'Right Ctrl', 0x20: 'Right Shift', 0x40: 'Right Alt', 0x80: 'Right GUI'
}

# Function to decode a USB HID packet (assuming standard 8-byte keyboard report)
def decode_usb_hid_packet(packet):
    # First byte is modifiers, second byte is reserved, following bytes are keycodes
    packet = packet.strip()  # Remove any trailing newlines or spaces
    if len(packet) == 0:
        return None

    # Convert hex string to bytes
    packet_bytes = bytes.fromhex(packet)

    if len(packet_bytes) < 3:  # We expect at least 3 bytes (modifier, reserved, key)
        return None

    # Decode modifier keys (if any)
    modifier_byte = packet_bytes[0]
    modifier_keys = [usb_hid_modifiers[bit] for bit in usb_hid_modifiers if modifier_byte & bit]

    # Decode key codes
    key_codes = packet_bytes[2:]  # Skip the second byte (reserved)
    keys = [usb_hid_keycodes.get(code, f"Unknown({code})") for code in key_codes if code != 0]

    return modifier_keys + keys

# Decode the packets from the tshark output file
decoded_packets = [decode_usb_hid_packet(packet) for packet in tshark_output_content if packet.strip()]

# Filter out any None results
decoded_packets = [packet for packet in decoded_packets if packet]

decoded_packets
