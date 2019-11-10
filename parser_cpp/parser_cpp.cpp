#include <iostream>
#include "json.hpp"

int main() {
	auto j = nlohmann::json::parse(std::cin);
}
