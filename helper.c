#include "portable8439.h"
#include "chacha-portable.h"
#include <stdlib.h>

#define RFC_8439_TAG_SIZE (16)
#define RFC_8439_KEY_SIZE (32)
#define RFC_8439_NONCE_SIZE (12)

int8_t encrypt(
  uint8_t *plain, int plain_text_size, uint8_t *ad, int ad_size, uint8_t *key, uint8_t *nonce, uint8_t *buffer
) {
  size_t cipher_size = portable_chacha20_poly1305_encrypt(buffer, key, nonce, ad, ad_size, plain, plain_text_size);
  return cipher_size;
}

int8_t decrypt(
  uint8_t *buffer2, uint8_t *key, uint8_t *nonce, uint8_t *ad, int ad_size, uint8_t *buffer, int cipher_size
) {
  return portable_chacha20_poly1305_decrypt(buffer2, key, nonce, ad, ad_size, buffer, cipher_size);
}
