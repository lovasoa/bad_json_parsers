#include <iostream>
#include "rapidjson/document.h"
#include "rapidjson/error/en.h"
#include "rapidjson/istreamwrapper.h"
 
using namespace rapidjson;

int main(void) {
  Document d;
  IStreamWrapper isw(std::cin);
  if (d.ParseStream(isw).HasParseError()) {
      fprintf(stderr, "error: %s\n", GetParseError_En(d.GetParseError()));
      return 1;
  }
  return 0;
}
