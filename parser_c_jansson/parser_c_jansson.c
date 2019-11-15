#include <jansson.h>
#include <stdio.h>

int main(int argc, char ** argv) {
  json_error_t error;
  json_t* j_test = json_loadf(stdin, JSON_DECODE_ANY, &error);
  if (j_test == NULL) {
    fprintf(stderr, "error at offset %d: %s\n", error.position, error.text);
    return 1;
  } else {
    return 0;
  }
}
