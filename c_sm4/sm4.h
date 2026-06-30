#ifndef SM4_H
#define SM4_H

#include <stdint.h>
#include <stddef.h>

void sm4_key_expansion(const uint8_t* key, uint32_t* rk);
void sm4_encrypt_block(const uint8_t* in, uint8_t* out, const uint32_t* rk);
void sm4_decrypt_block(const uint8_t* in, uint8_t* out, const uint32_t* rk);
void sm4_encrypt_cbc(const uint8_t* in, uint8_t* out, size_t len,
                      const uint32_t* rk, const uint8_t* iv);
void sm4_decrypt_cbc(const uint8_t* in, uint8_t* out, size_t len,
                      const uint32_t* rk, const uint8_t* iv);

#endif
