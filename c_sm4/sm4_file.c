#include "sm4.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int sm4_encrypt_file(const uint8_t* key, const char* input_path, const char* output_path) {
    FILE* fin = fopen(input_path, "rb");
    if (!fin) return -1;
    fseek(fin, 0, SEEK_END);
    long fsize = ftell(fin);
    fseek(fin, 0, SEEK_SET);

    uint8_t* in_data = (uint8_t*)malloc(fsize);
    fread(in_data, 1, fsize, fin);
    fclose(fin);

    size_t padded = ((fsize + 15) / 16) * 16;
    uint8_t* out_data = (uint8_t*)calloc(padded, 1);
    memcpy(out_data, in_data, fsize);
    uint8_t pad_val = padded - fsize;
    for (size_t i = fsize; i < padded; i++) out_data[i] = pad_val;

    uint32_t rk[32];
    uint8_t iv[16];
    memset(iv, 0x00, 16);

    sm4_key_expansion(key, rk);
    sm4_encrypt_cbc(out_data, out_data, padded, rk, iv);

    FILE* fout = fopen(output_path, "wb");
    if (!fout) { free(in_data); free(out_data); return -1; }
    fwrite(out_data, 1, padded, fout);
    fclose(fout);

    free(in_data);
    free(out_data);
    return 0;
}

int sm4_decrypt_file(const uint8_t* key, const char* input_path, const char* output_path) {
    FILE* fin = fopen(input_path, "rb");
    if (!fin) return -1;
    fseek(fin, 0, SEEK_END);
    long fsize = ftell(fin);
    fseek(fin, 0, SEEK_SET);

    uint8_t* in_data = (uint8_t*)malloc(fsize);
    fread(in_data, 1, fsize, fin);
    fclose(fin);

    uint8_t* out_data = (uint8_t*)calloc(fsize, 1);

    uint32_t rk[32];
    uint8_t iv[16];
    memset(iv, 0x00, 16);

    sm4_key_expansion(key, rk);
    sm4_decrypt_cbc(in_data, out_data, fsize, rk, iv);

    uint8_t pad_val = out_data[fsize - 1];
    size_t actual_size = fsize - pad_val;

    FILE* fout = fopen(output_path, "wb");
    if (!fout) { free(in_data); free(out_data); return -1; }
    fwrite(out_data, 1, actual_size, fout);
    fclose(fout);

    free(in_data);
    free(out_data);
    return 0;
}
