#include <iostream>
#include <cstdlib>
#include "json.hpp"

// for convenience
using json = nlohmann::json;

int main(void) {
	auto j = json::parse(std::cin);
}
