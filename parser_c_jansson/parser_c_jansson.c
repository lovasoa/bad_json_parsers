#include <jansson.h>
#include <stdio.h>

int main(int argc, char ** argv) {
  json_t* j_test = json_loadf(stdin, JSON_DECODE_ANY, NULL);
  return j_test == NULL ? 1 : 0;
}
