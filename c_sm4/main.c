#include "sm4.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if (argc < 4) {
        printf("Usage: %s <enc|dec> <input_file> <output_file> [key_hex]\n", argv[0]);
        return 1;
    }

    uint8_t key[16];
    if (argc >= 5) {
        for (int i = 0; i < 16; i++) {
            sscanf(argv[4] + 2*i, "%2hhx", &key[i]);
        }
    } else {
        memset(key, 0x01, 16);
    }

    FILE* fin = fopen(argv[2], "rb");
    if (!fin) { printf("Cannot open input file\n"); return 1; }
    fseek(fin, 0, SEEK_END);
    long fsize = ftell(fin);
    fseek(fin, 0, SEEK_SET);

    uint8_t* in_data = malloc(fsize);
    fread(in_data, 1, fsize, fin);
    fclose(fin);

    size_t padded = ((fsize + 15) / 16) * 16;
    uint8_t* out_data = calloc(padded, 1);
    memcpy(out_data, in_data, fsize);
    uint8_t pad_val = padded - fsize;
    for (size_t i = fsize; i < padded; i++) out_data[i] = pad_val;

    uint32_t rk[32];
    uint8_t iv[16];
    memset(iv, 0x00, 16);

    sm4_key_expansion(key, rk);

    if (strcmp(argv[1], "enc") == 0) {
        sm4_encrypt_cbc(out_data, out_data, padded, rk, iv);
    } else {
        sm4_decrypt_cbc(out_data, out_data, padded, rk, iv);
    }

    FILE* fout = fopen(argv[3], "wb");
    if (!fout) { printf("Cannot open output file\n"); free(in_data); free(out_data); return 1; }
    
    size_t write_size = (strcmp(argv[1], "enc") == 0) ? padded : fsize;
    fwrite(out_data, 1, write_size, fout);
    fclose(fout);

    free(in_data);
    free(out_data);
    printf("Operation completed successfully\n");
    return 0;
}
