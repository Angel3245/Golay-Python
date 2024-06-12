Basic Golay Error Correction Code Implementation
===

Golay codes are a class of error-correcting codes used to detect and correct errors in data transmission. This project provides a basic implementation of Golay error correction codes in Python, supporting both the Golay (24, 12, 8) and Golay (23, 12, 7) codes.

## Golay Codes
- Golay (24, 12, 8): This code encodes 12 bits of data into 24 bits by adding 12 parity bits. It can correct up to 3 errors in the 24-bit codeword.
- Golay (23, 12, 7): This code encodes 12 bits of data into 23 bits by adding 11 parity bits. It can correct up to 3 errors in the 23-bit codeword.

## Project Structure
The project is organized as follows:

```
├── Archivo.py
├── Codificar.py
├── Decodificar.py
├── Golay.py
├── Ruido.py
├── README.md
```

## Methodology
### Encoding
The encoding process involves:

- Generating parity bits: Calculating parity bits for the given 12-bit data.
- Forming the codeword: Appending the parity bits to the original data to form the 23-bit or 24-bit codeword.

### Decoding
The decoding process involves:

- Calculating the syndrome: Using the received codeword to detect errors.
- Error correction: Correcting the errors based on the syndrome.
- Extracting the original data: Removing the parity bits to retrieve the original 12-bit data.

### Adding Noise
Adding noise to the codeword involves:

- Flipping bits: Randomly flipping bits in the codeword to simulate transmission errors.

## Implementation Details
The implementation includes:

- Archivo.py: Handles file input/output operations.
- Golay.py: Contains the main Golay code implementation for both (24, 12, 8) and (23, 12, 7) codes.

- Codificar.py: Implements the encoding functionality. Use: ```python Codificar.py <file_path> <golay_type>```
- Decodificar.py: Implements the decoding functionality. Use: ```python Decodificar.py <file_path> <golay_type>```
- Ruido.py: Adds noise to the codewords to simulate transmission errors. Use: ```python Ruido.py <file_path>```