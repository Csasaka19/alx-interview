# UTF_8 validation using python

## UTF-8 encoding.

Valid UTF-8 sequences follow specific rules:

Single-byte characters: The most significant bit (MSB) of a single-byte character is always 0.

Multi-byte characters: The MSB of the first byte indicates the total number of bytes in the sequence (e.g., 110xxxxx for two-byte sequences, 1110xxxx for three-byte sequences, and 11110xxx for four-byte sequences). Subsequent bytes in a multi-byte sequence have their MSB set to 10xxxxxx.
